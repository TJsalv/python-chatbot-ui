from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "pythonchatbotui"

    from .index import index
    from .auth import auth 

    app.register_blueprint(index, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app 

