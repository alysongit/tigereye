from flask import Flask

from tigereye.api import ApiView

from tigereye.models import db,JsonEncode

def create_app():
    "创建一个flask app对象"
    app = Flask(__name__)

    app.config.from_object('tigereye.configs.default.DefaultConfig')

    app.json_encoder = JsonEncode
    # MovieView.register(app)
    # MiscView.register(app)
    # CinemaView.register(app)
    configure_views(app)
    db.init_app(app)
    return app


def configure_views(app):
    from tigereye.api.misc import MiscView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.movie import MovieView

    for view in locals().values():
        if type(view) == type and issubclass(view,ApiView):
            view.register(app)