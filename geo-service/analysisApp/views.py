from datetime import datetime
from flask import Flask, render_template,request

from .forms import *
from .models import *

from . import app


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route('/arenas/', methods=["GET","POST"])
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
        form.longitude = round(arena.longitude,4)
        form.latitude = round(arena.latitude,4)
        county=session.query(County).filter(County.geom.ST_Contains(arena.geom)).first()
        if county != None:
            district=session.query(District).filter(District.geom.ST_Intersects(arena.geom)).first()
            state = county.state_ref
            form.popup = """The {0} is located at {4}, {5}, which is in {1} County, {3}, and in {3} Congressional District {2}.""".format(arena.name,county.name, district.district, state.name, form.longitude, form.latitude)
        else:
            form.popup = """The county, district, and state could not be located using point in polygon analysis"""
        return render_template('map.html',form=form)
    return render_template('map.html',form=form)