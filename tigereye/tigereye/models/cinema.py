from tigereye.models import  db,Model

class Cinema(db.Model,Model):
    """"""
    """cid,影院ID,主键"""
    cid = db.Column(db.Integer,primary_key=True)
    """影院名称"""
    name = db.Column(db.String(64),unique=True,nullable=False)
    """影院地址"""
    address = db.Column(db.String(128),nullable=False)
    halls=db.Column(db.Integer,default=0,nullable=False)
    handle_free = db.Column(db.Integer,default=0,nullable=False)
    buy_limit = db.Column(db.Integer,default=0,nullable=False)
    status=db.Column(db.Integer,default=0,nullable=False,index=True)
