from tigereye.models import db,Model
class Hall(db.Model,Model):
    hid = db.Column(db.Integer,primary_key=True)

    """cid,影院ID,主键"""
    cid = db.Column(db.Integer)
    """影院名称"""
    name = db.Column(db.String(64), unique=True, nullable=False)

    screen_type =db.Column(db.String(32))
    audio_type = db.Column(db.String(32))
    seats_num =db.Column(db.Integer,default=0,nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False, index=True)