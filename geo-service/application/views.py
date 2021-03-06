from datetime import datetime
from flask import render_template, request, jsonify, redirect, send_file
import logging
from werkzeug.utils import secure_filename
import os
from .forms import AddForm
from flask_oidc import OpenIDConnect
from flask_zipkin import Zipkin
import shapely
from geoalchemy2.shape import to_shape
import geopandas as gpd
import zipfile
from zipfile import ZipFile

from .forms import *
from .models import *
from application import app


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('flask_cors').level = logging.DEBUG
oidc = OpenIDConnect(app)
zipkin = Zipkin(app, sample_rate=100)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,PATCH,OPTIONS')
    return response

# APIs return views

@app.route('/geo-api/login/')
@oidc.require_login
def login():
    return 'Welcome %s' % oidc.user_getfield('email')


@app.route('/geo-api/logout/')
def logout():
    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'


@app.route("/geo-api/")
def home():
    return render_template("home.html")


@app.route("/geo-api/about/")
def about():
    return render_template("about.html")


@app.route("/geo-api/contact/")
def contact():
    return render_template("contact.html")


@app.route("/geo-api/hello/")
@app.route("/geo-api/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route('/geo-api/arenas/', methods=["GET", "POST"])
def arenas():
    form = ArenaForm(request.form)
    arenas = session.query(Arena).all()
    form.selections.choices = [(arena.id, arena.name) for arena in arenas]
    form.popup = "Select an Arena"
    form.latitude = 38.89517
    form.longitude = -77.03682
    if request.method == "POST":
        arena_id = form.selections.data
        arena = session.query(Arena).get(arena_id)
        form.longitude = round(arena.longitude, 4)
        form.latitude = round(arena.latitude, 4)
        county = session.query(County).filter(
            County.geom.ST_Contains(arena.geom)).first()
        if county != None:
            district = session.query(District).filter(
                District.geom.ST_Intersects(arena.geom)).first()
            state = county.state_ref
            form.popup = """The {0} is located at {4}, {5}, which is in {1} County, {3}, and in {3} Congressional District {2}.""".format(
                arena.name, county.name, district.district, state.name, form.longitude, form.latitude)
        else:
            form.popup = """The county, district, and state could not be located using point in polygon analysis"""
        return render_template('map.html', form=form)
    return render_template('map.html', form=form)

# REST APIs


@app.route("/geo-api/v0.1/data_test/")
def get_data():
    return app.send_static_file("data.json")


@app.route('/geo-api/v0.1/', methods=['GET'])
def get_endpoints():
    data = [{'name': "Arena", "endpoint": "/arena"},
            {'name': "State", "endpoint": "/state"},
            {'name': "County", "endpoint": "/county"},
            {'name': "District", "endpoint": "/district"},
            {'name': "Utility", "endpoint": "/util"}]
    return jsonify({"endpoints": data})


@app.route('/geo-api/v0.1/arena/', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def get_arenas():
    if 'name' in request.args:
        arenas = session.query(Arena).filter(name=request.args['name'])
    else:
        arenas = session.query(Arena).all()
        data = [{"type": "Feature", "properties": {"name": arena.name, "id": arena.id}, "geometry": {"type": "Point", "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]},
                } for arena in arenas]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/arena/<int:arena_id>/', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def get_arena(arena_id):
    arena = session.query(Arena).get(arena_id)
    if arena != None:
        data = [{"type": "Feature",
                 "properties": {"name": arena.name, "id": arena.id},
                 "geometry": {"type": "Point",
                              "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]},
                 }]
    else:
        data = []
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/arena/<arena_name>/', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def get_arena_name(arena_name):
    arenas = session.query(Arena).filter(Arena.name.like(arena_name+"%")).all()
    data = [{"type": "Feature", "properties": {"name": arena.name}, "geometry": {"type": "Point", "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]},
             } for arena in arenas]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/arena/<int:arena_id>/intersect/', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def arena_intersect(arena_id):
    arena = session.query(Arena).get(arena_id)
    county = session.query(County).filter(
        County.geom.ST_Intersects(arena.geom)).first()
    district = session.query(District).filter(
        District.geom.ST_Intersects(arena.geom)).first()
    if county != None:
        data = [{"type": "Feature", "properties": {"name": arena.name, "id": arena.id, },
                 "geometry": {"type": "Point", "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]},
                 }, {"type": "Feature", "properties": {"name": county.name, "id": county.id, },
                     "geometry": {"type": "MultiPolygon",
                                  "coordinates": [shapely.geometry.geo.mapping(to_shape(county.geom))]},
                     }, {"type": "Feature", "properties": {"name": district.district, "id": district.id, },
                "geometry": {"type": "MultiPolygon",
                         "coordinates": [shapely.geometry.geo.mapping(to_shape(district.geom))]},
                         }, {"type": "Feature", "properties": {"name": county.state_ref.name, "id": county.state_ref.id, },
                "geometry": {"type": "MultiPolygon",
                             "coordinates": [shapely.geometry.geo.mapping(to_shape(county.state_ref.geom))]},
                             }
                ]
        return jsonify({"type": "FeatureCollection", "features": data})
    else:
        return redirect('/api/v0.1/arena/' + str(arena_id))


@app.route('/geo-api/v0.1/arena/add/', methods=['GET', 'POST'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def add_arenas():
    form = AddForm(request.form)
    form.name.data = "New Arena"
    form.longitude.data = -121.5
    form.latitude.data = 37.8

    if request.method == "POST":
        arena = Arena()
        json = request.get_json(force=True, silent=True)

        if (json == None):  # Post request using Form submit
            arena.name = request.form['name']
            arena.longitude = float(request.form['longitude'])
            arena.latitude = float(request.form['latitude'])
        else:  # Post request using Json Payload
            arena.name = json['name']
            arena.longitude = float(json['longitude'])
            arena.latitude = float(json['latitude'])

        arena.geom = 'SRID=4326;POINT({0} {1})'.format(
            arena.longitude, arena.latitude)
        session.add(arena)
        session.commit()
        data = [{"type": "Feature", "properties": {"name": arena.name}, "geometry": {
            "type": "Point", "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]}, }]
        return jsonify({'added': 'success', "type": "FeatureCollection", "features": data})
    return render_template('addarena.html', form=form)


@app.route('/geo-api/v0.1/arena/delete/<int:arena_id>/', methods=['DELETE'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def delete_arena(arena_id):
    arena = session.query(Arena).filter(
        Arena.id == arena_id).delete(synchronize_session='fetch')
    session.commit()
    return jsonify({"deleted": "success"})


@app.route('/geo-api/v0.1/county/', methods=['GET'])
def get_counties():
    counties = session.query(County).all()
    # print(counties)
    geoms = {county.id: shapely.geometry.geo.mapping(
        to_shape(county.geom)) for county in counties}
    data = [{"type": "Feature",
             "properties": {"name": county.name, "state": county.state.name},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": geoms[county.id]["coordinates"]},
             } for county in counties]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/county/query/size/<float:size>/', methods=['GET'])
def get_county_size(size):
    counties = session.query(County).filter(County.geom.ST_Area() > size).all()
    data = [{"type": "Feature", "properties": {"name": county.name, "id": county.id, "state": county.state.name, "area": to_shape(county.geom).area},
             "geometry": {"type": "MultiPolygon", "coordinates": [shapely.geometry.geo.mapping(to_shape(county.geom))["coordinates"]]}, } for county in counties]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/county/<int:county_id>/', methods=['GET'])
def get_county(county_id):

    county = session.query(County).get(county_id)
    shp = to_shape(county.geom)
    geojson = shapely.geometry.geo.mapping(shp)
    data = [{"type": "Feature",
             "properties": {"name": county.name, "state": county.state.name},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [geojson]},  # "["+str(rnd(arena.geom.x,5)) + str(rnd(arena.geom.x,5))+"]"
             }]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/county/<county_name>/', methods=['GET'])
def get_county_name(county_name):
    counties = session.query(County).filter(
        County.name.like(county_name+"%")).all()
    data = [{"type": "Feature",
             "properties": {"name": county.name,  "state": county.state.name},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [shapely.geometry.geo.mapping(to_shape(county.geom))["coordinates"]]},
             } for county in counties]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/state/', methods=['GET'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def get_states():
    states = session.query(State).all()
    data = [{"type": "Feature",
             "properties": {"state": state.name, "id": state.id},
             "geometry": {"type": "MultiPolygon", "coordinates": "[Truncated]"}, } for state in states]
    if "geometry" in request.args.keys():
        if request.args["geometry"] == '1' or request.args["geometry"] == 'True':
            data = [{"type": "Feature", "properties": {"state": state.name, "id": state.id}, "geometry": {
                "type": "MultiPolygon", "coordinates": [shapely.geometry.geo.mapping(to_shape(state.geom))["coordinates"]]}, } for state in states]

    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/state/<int:state_id>/', methods=['GET'])
def get_state(state_id):

    state = session.query(State).get(state_id)
    shp = to_shape(state.geom)
    geojson = shapely.geometry.geo.mapping(shp)
    data = [{"type": "Feature",
             "properties": {"name": state.name, "id": state.id},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [geojson]},
             }]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/state/<int:state_id>/within/', methods=['GET'])
def get_state_arenas(state_id):

    state = session.query(State).get(state_id)
    shp = to_shape(state.geom)
    geojson = shapely.geometry.geo.mapping(shp)
    data = [{"type": "Feature",
             "properties": {"name": state.name, "id": state.id},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [geojson]},
             }]
    arenas = session.query(Arena).filter(Arena.geom.ST_Within(state.geom))
    data_arenas = [{"type": "Feature",
                    "properties": {"name": arena.name},
                    "geometry": {"type": "Point",
                                 "coordinates": [round(arena.longitude, 6), round(arena.latitude, 6)]},
                    } for arena in arenas]
    data.extend(data_arenas)
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/state/<state_name>/', methods=['GET'])
def get_state_name(state_name):
    states = session.query(State).filter(State.name.like(state_name+"%")).all()
    data = [{"type": "Feature",
             "properties": {"state": state.name, "id": state.id},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [shapely.geometry.geo.mapping(to_shape(state.geom))["coordinates"]]},
             } for state in states]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/district/', methods=['GET'])
def get_districts():
    districts = session.query(District).all()
    if 'geometry' in request.args.keys() and request.args['geometry'] in ('1', 'True'):
        data = [{"type": "Feature",
                 "properties": {"representative": district.name, "district": district.district,
                                "state": district.state_ref.name, "id": district.id},
                 "geometry": {"type": "MultiPolygon",
                              "coordinates": shapely.geometry.geo.mapping(to_shape(district.geom))["coordinates"]},
                 } for district in districts]
    else:
        data = [{"type": "Feature",
                 "properties": {"representative": district.name, "district": district.district,
                                "state": district.state_ref.name, "id": district.id},
                 "geometry": {"type": "MultiPolygon",
                              "coordinates": ["Truncated"]},
                 } for district in districts]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/district/<int:district_id>/', methods=['GET'])
def get_district(district_id):

    district = session.query(District).get(district_id)
    shp = to_shape(district.geom)
    geojson = shapely.geometry.geo.mapping(shp)
    data = [{"type": "Feature",
             "properties": {"district": district.district, "id": district.id},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": [geojson]},
             }]
    return jsonify({"type": "FeatureCollection", "features": data})


@app.route('/geo-api/v0.1/district/<district_name>/', methods=['GET'])
def get_district_name(district_name):

    districts = session.query(District).filter(
        District.name.like(district_name+"%")).all()
    geoms = {district.id: shapely.geometry.geo.mapping(to_shape(district.geom))
             for district in districts}

    data = [{"type": "Feature",
             "properties": {"state": district.name},
             "geometry": {"type": "MultiPolygon",
                          "coordinates": geoms[district.id]["coordinates"]},
             } for district in districts]
    return jsonify({"type": "FeatureCollection", "features": data})


# Utility APIs
ALLOWED_EXTENSIONS = {'zip', 'shp', 'geojson', 'csv', 'dgn', 'dxf'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/geo-api/v0.1/util/', methods=['GET'])
def get_utilities():
    return jsonify({"status": "ongoing"})


@app.route('/geo-api/v0.1/util/uploadfile/', methods=['GET', 'POST'])
# @oidc.accept_token(require_token=True, scopes_required=['openid'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return 'No filename'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.getcwd())
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("saved file successfully")
            # send file name as parameter to downlad
            return 'File Uploaded! That is OK.'
    return 'File error or file type is not supported to upload'


@app.route("/geo-api/v0.1/util/list-uploaded/", methods=['GET'])
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route("/geo-api/v0.1/util/downloadfile/<filename>/", methods=['GET'])
def download_file(filename):
    value = filename
    return render_template('download.html', value=value)


@app.route('/geo-api/v0.1/util/return-files/<filename>/')
def return_files_tut(filename):
    print(os.getcwd())
    print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file_path = os.path.join(
        os.getcwd(), app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, mimetype='application/zip', as_attachment=True, attachment_filename=filename)


@app.route('/geo-api/v0.1/util/convertofile/', methods=['GET', 'POST'])
def convert_to_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return 'No filename'
        if file and allowed_file(file.filename):
            # else:
            uploadFileName = secure_filename(file.filename)
            srcFileName = os.path.join(
                app.config['UPLOAD_FOLDER'], uploadFileName)
            file.save(srcFileName)

            ext = srcFileName.rsplit('.', 1)[1].lower()
            base = srcFileName.rsplit('.', 1)[0]
            # If Shape files in zip, select .shp
            if ext == 'zip':
                with ZipFile(srcFileName, 'r') as zip_ref:
                    zip_ref.extractall(app.config['UPLOAD_FOLDER'])
                srcFileName = base + '.shp'

            print(srcFileName)

            # Create target file temporarily at current folder using name from source file and new format
            targetFormat = request.form['format']
            targetFilename = uploadFileName.rsplit('.', 1)[0] + '.' + targetFormat

            print(targetFilename)

            df = gpd.read_file(srcFileName)
            if targetFormat == 'csv':
                df.to_csv(path_or_buf=targetFilename,
                          sep='\t', encoding='utf-8')
            if targetFormat == 'geojson':
                df.to_file(driver='GeoJSON', filename=targetFilename)

            # Zip file and save to Uploads folder before return to clients
            zipToDownload = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename + '.zip')
            zipf = ZipFile(zipToDownload, "w", zipfile.ZIP_DEFLATED)
            zipf.write(targetFilename)
            zipf.close()
            # Delete the target temporary file 
            os.remove(targetFilename)
            for f in os.listdir(app.config['UPLOAD_FOLDER']):
                if f.endswith(".zip"):
                    continue
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

            return jsonify({"convert": "success",  "filename": targetFilename + '.zip'})
    return jsonify({"convert": "failed"})

# @zipkin.transport_handler
# def default_handler(encoded_span):
#     return requests.post(
# 		app.config['ZIPKIN_DSN'],
#         data=encoded_span,
#         headers={'Content-Type': 'application/x-thrift'},
# )