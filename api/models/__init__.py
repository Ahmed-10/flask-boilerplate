from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Model:
    def add(self):
        db.session.add(self)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def add_many(records):
        db.session.bulk_save_objects(records, return_defaults=True)
        db.session.commit()

    def update(self):
        db.session.commit()

    def remove(self):
        db.session.delete(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def delete_many(self, list_of_ids):
        statement = self.model.__table__.delete().\
            where(self.model.id.in_(list_of_ids))
        db.session.execute(statement)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

class Category(db.Model, Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
        }