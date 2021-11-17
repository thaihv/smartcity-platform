import flask
import logging
from flask_cors import CORS
import py_eureka_client.eureka_client as eureka_client

# rest_port = 5000
# eureka_client.init(eureka_server="http://localhost:8761/eureka", app_name="geo-service", instance_host="localhost", instance_port=rest_port)
# #conn_string = 'postgresql://postgres:postgres@localhost:5432/geospatial'
# conn_string = 'postgresql://postgres:postgres@174.138.25.165:25432/geospatial'

# for production
rest_port = 5000
eureka_client.init(eureka_server="http://discovery:8761/eureka", app_name="geo-service", instance_port=rest_port)
conn_string = 'postgresql://postgres:postgres@geospatial:5432/geospatial'

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/geo-api/*": {"origins": "*"}})
logging.getLogger('flask_cors').level = logging.DEBUG

# app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
# app.config['SECRET_KEY'] = "SECRET_KEY"
# app.config['DEBUG'] = True
# app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
# app.config['OIDC_OPENID_REALM'] = 'Smartcity'
# app.config['OIDC_INTROSPECTION_AUTH_METHOD'] = 'client_secret_post'
# app.config['OIDC_TOKEN_TYPE_HINT'] = 'access_token'
# app.config['OIDC-SCOPES'] = ["openid","email","profile"]
app.config.update({
    'SQLALCHEMY_DATABASE_URI': conn_string,
    'SECRET_KEY': 'SECRET_KEY',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_RESOURCE_SERVER_ONLY': True,
    'OIDC_OPENID_REALM': 'Smartcity',
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC-SCOPES': ["openid", "email", "profile"]
})

import application.views