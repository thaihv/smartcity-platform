import flask
import py_eureka_client.eureka_client as eureka_client

# rest_port = 5000
# eureka_client.init(eureka_server="http://localhost:8761/eureka",
#                    app_name="geo-service",
#                    instance_port=rest_port)

app = flask.Flask(__name__)

conn_string = 'postgresql://postgres:postgres@localhost:5432/geospatial'
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
    'OIDC_RESOURCE_SERVER_ONLY': False,
    'OIDC_OPENID_REALM': 'Smartcity',
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC-SCOPES': ["openid", "email", "profile"]
})

import application.views