from tigereye.configs.default import DefaultConfig


class ProductionConfig(DefaultConfig):
    DEBUG = False
    SQLALCHEMY_ECHO =False

    EMAIL_HOST = 'smtp.exmail.qq.com'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = SERVER_EMAIL = DEFAULT_SERVER_EMAIL ='test1@iguye.com'
    EMAIL_HOST_PASSWORD ='P67844QUssW3'
    EMAIL_USE_SSL = True
    # ADMINS=['guye@iguge.com']
    # ADMINS = ['1329387117@qq.com']
    # ADMINS = ['18052063223@163.com']
    # ADMINS = ['649299546@qq.com']
    # ADMINS = ['1065497532@qq.com']
    ADMINS = ['649299546@qq.com']
    # ADMINS = ['18052063223@163.com','18701552372@163.com']
    # ADMINS = ['18701552372@163.com']