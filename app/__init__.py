from flask import Flask
from flask_socketio import SocketIO
from gevent import monkey

import app

monkey.patch_all()  # Required for gevent to work properly

socketio = SocketIO(app, async_mode='gevent')



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    from .routes import bp
    app.register_blueprint(bp)
    socketio.init_app(app)
    return app