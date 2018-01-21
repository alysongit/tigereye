from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Model(object):
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