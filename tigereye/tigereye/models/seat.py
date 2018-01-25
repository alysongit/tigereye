from enum import Enum
from sqlalchemy import text
from datetime import datetime
from tigereye.models import db,Model


class SeatType(Enum):
    #过道
    road = 0
    #单座
    single = 1
    #情侣座
    couple = 2

class SeatStatus(Enum):
    #正常
    ok = 0
    #锁定
    locked = 1
    #售出
    sold = 2
    #已取票
    printed = 3


class Seat(db.Model,Model):
    sid = db.Column(db.Integer,primary_key=True)
    hid = db.Column(db.Integer)
    cid = db.Column(db.Integer)

    x = db.Column(db.Integer,default=0,nullable=False)
    y = db.Column(db.Integer, default=0, nullable=False)
    row = db.Column(db.String(8))
    column = db.Column(db.String(8))

    area = db.Column(db.String(16))
    seat_type = db.Column(db.String(16))
    love_seats = db.Column(db.String(32))
    status = db.Column(db.Integer, default=0, nullable=False, index=True)



class PlaySeat(db.Model,Model):
    psid = db.Column(db.Integer,primary_key=True)
    orderno = db.Column(db.String(32),index=True)
    pid = db.Column(db.Integer, nullable=False)
    sid = db.Column(db.Integer,nullable=False)
    cid = db.Column(db.Integer, nullable=False)
    hid = db.Column(db.Integer, nullable=False)

    x = db.Column(db.Integer,default=0,nullable=False)
    y = db.Column(db.Integer, default=0, nullable=False)
    row = db.Column(db.String(8))
    column = db.Column(db.String(8))

    area = db.Column(db.String(16))
    seat_type = db.Column(db.String(16))
    love_seats = db.Column(db.String(32))
    locked_time = db.Column(db.DateTime)
    created_time = db.Column(db.DateTime,server_default=text("CURRENT_TIMESTAMP"))
    status = db.Column(db.Integer, default=0, nullable=False, index=True)

    #将seat对象中的信息拷贝到playseat对象中
    def copy(self,seat):
        self.sid = seat.sid
        self.cid = seat.cid
        self.hid = seat.hid
        self.x = seat.x
        self.y = seat.y
        self.row = seat.row
        self.column = seat.column
        self.area = seat.area
        self.love_seats = seat.love_seats
        self.seat_type = seat.seat_type
        self.status = seat.status


    @classmethod
    def lock(cls,orderno,pid,sid_list):
        #创建数据库session
        session = db.create_scoped_session()
        #查询出pid,status,sid符合锁定条件的座位
        rows = session.query(PlaySeat).filter(
            PlaySeat.pid == pid,
            PlaySeat.status == SeatStatus.ok.value,
            PlaySeat.sid.in_(sid_list)
        #更新座位信息
        ).update({
            "orderno":orderno,
            "status":SeatStatus.locked.value,
            "locked_time":datetime.now()
        },synchronize_session=False)
        #如果更新的行数与传入的座位数量不符,则回滚
        if rows != len(sid_list):
            session.rollback()
            return 0
        #如果数量符合,则提交,并返回锁定的座位数量
        session.commit()
        return rows

    @classmethod
    def unlock(cls,orderno,pid,sid_list):
        session = db.create_scoped_session()
        rows = session.query(PlaySeat).filter_by(
            orderno = orderno,
            status = SeatStatus.locked.value
        ).update({
            "orderno" : None,
            "status" : SeatStatus.ok.value
        },synchronize_session=False)
        if rows != len(sid_list):
            session.rollback()
            return 0
        #如果数量符合,则提交,并返回锁定的座位数量
        session.commit()
        return rows

    @classmethod
    def buy(cls, orderno, pid, sid_list):
        session = db.create_scoped_session()
        rows = session.query(PlaySeat).filter_by(
            orderno=orderno,
            status=SeatStatus.locked.value
        ).update({
            # "orderno": None,
            "status": SeatStatus.sold.value
        }, synchronize_session=False)
        if rows != len(sid_list):
            session.rollback()
            return 0
        # 如果数量符合,则提交,并返回锁定的座位数量
        session.commit()
        return rows

    @classmethod
    def refund(cls,orderno,pid,sid_list):
        session = db.create_scoped_session()
        rows = session.query(PlaySeat).filter_by(
            orderno=orderno,
            status=SeatStatus.sold.value
        ).update({
             #将订单号设为空
            "status": SeatStatus.ok.value , #修改座位状态为正常
            "orderno": None,
        }, synchronize_session=False)
        if rows != len(sid_list):
            session.rollback()
            return 0
        # 如果数量符合,则提交,并返回锁定的座位数量
        session.commit()
        return rows

    @classmethod
    def print_tickets(cls,orderno,pid,sid_list):
        session = db.create_scoped_session()
        rows = session.query(PlaySeat).filter_by(
            orderno=orderno,
            status=SeatStatus.sold.value
        ).update({
            # 将订单号设为空
            "status": SeatStatus.printed.value,  # 修改座位状态为正常
            # "orderno": None,
        }, synchronize_session=False)
        if rows != len(sid_list):
            session.rollback()
            return 0
        # 如果数量符合,则提交,并返回锁定的座位数量
        session.commit()
        return rows