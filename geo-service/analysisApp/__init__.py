import flask
app = flask.Flask(__name__)

conn_string = 'postgresql://postgres:postgres@localhost:5432/geospatial'
#conn_string = 'postgresql://postgres:postgres@tamky.xyz:25432/geospatial'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SECRET_KEY'] = "SECRET_KEY"
app.config['DEBUG'] = True