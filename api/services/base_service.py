from flask import abort
from sqlalchemy.exc import IntegrityError


class Service:
    def __init__(self, model):
        self.model = model

    def get_all_by(self, options):
        records = self.model.query.filter_by(**options).all()
        return [record.format() for record in records]

    def get_one_by(self, options):
        record = self.model.query.filter_by(**options).first_or_404()
        return record.format()

    def get_all(self):
        records = self.model.query.all()
        return [record.format() for record in records]

    def get_all_by_company(self, company_id):
        options = {"company_id": company_id}
        return self.get_all_by(options)

    def get_one(self, id):
        record = self.model.query.get_or_404(id)
        return record.format()

    def add_one(self, new_record):
        record = self.model(**new_record)
        try:
            record.insert()
        except IntegrityError as error:
            record.rollback()
            abort(422, str(error.orig))
        return record.format()

    def add_many(self, list_of_records):
        records = []
        for item in list_of_records:
            records.append(self.model(item))
        try:
            self.model.add_many(records)
            return [record.format() for record in records]
        except IntegrityError as error:
            self.model.rollback()
            abort(422, str(error.orig))

    def update_one(self, id, data):
        record = self.model.query.get_or_404(id)
        for field, value in data.items():
            setattr(record, field, value)
        try:
            record.update()

        except IntegrityError as error:
            record.rollback()
            abort(422, error._message())

        return record.format()

    def del_one(self, id):
        record = self.model.query.get_or_404(id)
        record.delete()

    def del_many(self, list_of_ids):
        self.model.delete_many(self, list_of_ids)
