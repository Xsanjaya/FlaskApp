from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from models import db
from routes.api import api_route
from routes.api.UserRoute import user_route
from routes.api.AuthRoute import auth_route
from routes.web import web_route
from config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)

### ROUTE API ###
app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(auth_route, url_prefix='/api/auth')
app.register_blueprint(user_route, url_prefix='/api/users')


### ROUTE WEB ###
app.register_blueprint(web_route)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
