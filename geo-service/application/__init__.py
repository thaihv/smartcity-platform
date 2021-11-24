import flask
import os
import logging
from flask_cors import CORS
import py_eureka_client.eureka_client as eureka_client
from requests.auth import HTTPBasicAuth
from config.spring import ConfigClient
from werkzeug.exceptions import HTTPException

address = os.getenv('CONFIG_URI', 'http://localhost:8888')
profile = os.getenv('PROFILE', 'development')

config_client = ConfigClient(
    app_name = 'geo-service',
    address = address,
    branch = 'master',
    profile = profile,
    url = "{address}/{branch}/{app_name}-{profile}.yml"
)
response = config_client.get_config(auth=HTTPBasicAuth("jamescrafts80", "p4thaihv"))
print(config_client.config)

rest_port = config_client.get_attribute('server.port')
eureka_server = config_client.get_attribute('eureka.client.serviceUrl.defaultZone')
contextpath = config_client.get_attribute('server.servlet.context-path')
conn_string = config_client.get_attribute('conn_string')
instance_host = config_client.get_attribute('instance_host')
app_name = config_client.get_attribute('app_name')



eureka_client.init(eureka_server=eureka_server, app_name=app_name, instance_host=instance_host, instance_port=rest_port)

app = flask.Flask(__name__)
cors = CORS(app, resources={contextpath + '/*': {"origins": "*"}})
logging.getLogger('flask_cors').level = logging.DEBUG


UPLOAD_FOLDER = 'uploads/'
app.config.update({
    'SQLALCHEMY_DATABASE_URI': conn_string,
    'SECRET_KEY': 'SECRET_KEY',
    'TESTING': True,
    'DEBUG': True,
    'UPLOAD_FOLDER': UPLOAD_FOLDER,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_RESOURCE_SERVER_ONLY': True,
    'OIDC_OPENID_REALM': 'Smartcity',
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC-SCOPES': ["openid", "email", "profile"]
})

import application.views