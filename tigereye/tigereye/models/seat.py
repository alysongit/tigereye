from tigereye.models import db,Model
class Seat(db.Model,Model):
    sid = db.Column(db.Integer,primary_key=True)
    hid = db.Column(db.Integer)
    cid = db.Column(db.Integer)
    x = db.Column(db.Integer,default=0,nullable=False)
    y = db.Column(db.Integer, default=0, nullable=False)
    row =db.Column(db.String(8))
    colum = db.Column(db.String(8))
    area = db.Column(db.String(16))
    seat_type =db.Column(db.String(16))
    love_seats=db.Column(db.String(32))
    status = db.Column(db.Integer, default=0, nullable=False, index=True)