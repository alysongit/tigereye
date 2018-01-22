from tigereye.models import db,Model

class Movie(db.Model,Model):

    """电影信息表"""

    """电影ID，主键"""
    mid = db.Column(db.Integer,primary_key=True)

    """电影名称"""
    name = db.Column(db.String(64),nullable=False)

    """语言"""
    language = db.Column(db.String(32))

    """字幕"""
    subtitle = db.Column(db.String(32))

    """上映时间"""
    show_date = db.Column(db.Date)

    """电影格式"""
    mode =db.Column(db.String(16))
    """放映类型"""
    vision = db.Column(db.String(16))

    screen_size = db.Column(db.String(16))

    introduction = db.Column(db.Text)

    status = db.Column(db.Integer,default=0,nullable=False,index=True)