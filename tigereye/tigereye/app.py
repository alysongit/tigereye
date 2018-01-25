import logging
from logging import FileHandler

import os
from logging.handlers import SMTPHandler

from flask import Flask

from tigereye.api import ApiView
from tigereye.models import db, JsonEncoder


def create_app(config=None):
    """创建一个flask app对象并返回"""
    app = Flask(__name__)
    # app.debug = True
    # 读取配置文件
    app.config.from_object('tigereye.configs.default.DefaultConfig')
    app.config.from_object(config)
    app.json_encoder = JsonEncoder
    configue_views(app)
    # 初始化sqlalchemy配置
    db.init_app(app)

    #配置日志
    if not app.debug:
        app.logger.setLevel(logging.INFO)

        mail_hander = SMTPHandler(
            app.config['EMAIL_HOST'],
            app.config['SERVER_EMAIL'],
            app.config['ADMINS'],
            'TIGEREYE ALERT',
            credentials=(app.config['EMAIL_HOST_USER'],
                         app.config['EMAIL_HOST_PASSWORD'])
        )
        mail_hander.setLevel(logging.ERROR)
        mail_hander.setFormatter(logging.Formatter('''
        
        Message type: %(levelname)s
        Location:     %(pathname)s:%(lineno)d
        Module:       %(module)s
        Function:     %(funcName)s
        Time:         %(asctime)s
        
        Message:
        
        %(message)s       
        
        '''))
        app.logger.addHandler(mail_hander)

        file_handler = FileHandler(os.path.join(app.config['LOG_DIR'],'app.log'))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
        ))
        app.logger.addHandler(file_handler)

    app.logger.info('app created. BASE_DIR=%s' % app.config['BASE_DIR'])
    return app

def configue_views(app):
    from tigereye.api.misc import MiscView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.movie import MovieView
    from tigereye.api.play import PlayView
    from tigereye.api.seat import SeatView
    from tigereye.api.order import OrderView


    # 注册view到app中
    for view in locals().values():
        if type(view) == type and issubclass(view, ApiView):
            view.register(app)
