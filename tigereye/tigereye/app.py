from flask import Flask
from tigereye.api.misc import MiscView
from tigereye.api.cinema import CinemaView
from tigereye.models import db

def create_app():
    """创建一个flask app对象并返回"""
    app = Flask(__name__)
    # app.debug = True
    #读取配置文件
    app.config.from_object('tigereye.configs.default.DefaultConfig')
    #注册view到app中
    MiscView.register(app)
    CinemaView.register(app)
    #初始化sqlalchemy配置
    db.init_app(app)
    return app

# app = create_app()
#
# @app.route('/hello/')
# def hello():
#     return "hello tigereye"
#
# if __name__=='__main__':
#     app.run()