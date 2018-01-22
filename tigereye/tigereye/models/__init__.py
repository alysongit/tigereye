from flask_sqlalchemy import SQLAlchemy
from flask import  json as _json
db = SQLAlchemy()

class Model(object):


    @classmethod
    def get(cls,primary_key):
        return cls.query.get(primary_key)

    def put(self):
        db.session.add(self)


    def commit(self):
        db.session.commit()


    def rollback(self):
        db.session.rollback()


    def save(self):
        try:
            self.put()
            self.commit()
        except Exception:
            self.rollback()
            raise

    def delete(self):
        db.session.delete(self)

    def __json__(self):
        _d = {}
        for k, v in vars(self).items():
            if k.startswith('_'):
                continue
            _d[k] = v
        return _d


class JsonEncode(_json.JSONEncoder):
    """重载flask的JSONEncoder类"""
    def default(self,o):
        """重载default方法，以支持Model类对象的json序列化"""
        if isinstance(o,Model):
            return  o.__json__()
        return _json.JSONEncoder.default(self,o)