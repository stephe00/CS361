from flask import flask

def create_app():
    app = Flask(_name_)
    app.config['SECRET_KEY'] = 'sharkytank'

    from .views import views

    app.register_blueprint(views, url_prefix"/")
    return app
