from sqlalchemy import Enum
from tigereye.models import db,Model

class SeatType(Enum):
    road =0#过道
    single =1#单人
    couple =2#双人


class Seat(db.Model,Model):
    """物理座位表"""
    sid = db.Column(db.Integer,primary_key=True)  #座位ID，主键
    hid = db.Column(db.Integer)  #影厅ID
    cid = db.Column(db.Integer)  #影院ID
    x = db.Column(db.Integer,default=0,nullable=False)    #X坐标
    y = db.Column(db.Integer, default=0, nullable=False)   #Y坐标
    row =db.Column(db.String(8))    #显示的行名称
    colum = db.Column(db.String(8))   #显示的列名称
    area = db.Column(db.String(16))   #区域
    seat_type =db.Column(db.String(16))   #座位类型
    love_seats=db.Column(db.String(32))   #是否是情侣座位
    status = db.Column(db.Integer, default=0, nullable=False, index=True)   #状态



class PlaySeat(db.Model,Model):
    """排期座位表"""
    psid =db.Column(db.Integer,primary_key=True)
    orderno =db.Column(db.String(32),index=True)
    sid=db.Column(db.Integer,nullable=False)
    pid=db.Column(db.Integer,nullable=False)
    cid=db.Column(db.Integer,nullable=False)
    hid=db.Column(db.Integer,nullable=False)
    x = db.Column(db.Integer, default=0, nullable=False)
    y = db.Column(db.Integer, default=0, nullable=False)
    row = db.Column(db.String(8))
    colum = db.Column(db.String(8))
    area = db.Column(db.String(16))
    seat_type = db.Column(db.String(16))
    love_seats = db.Column(db.String(32))
    status = db.Column(db.Integer, default=0, nullable=False, index=True)

    def copy(self,seat):
        self.sid=seat.sid
        self.cid=seat.cid
        self.hid=seat.hid
        self.x=seat.x
        self.y=seat.y
        self.row=seat.row
        self.colum=seat.colum
        self.area=seat.area
        self.love_seats=seat.love_seats
        self.seat_type = seat.seat_type
        self.status=seat.status
