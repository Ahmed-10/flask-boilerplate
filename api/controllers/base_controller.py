from flask import jsonify


class Controller:
    def __init__(self, service):
        self.service = service()

    def all(self):
        return jsonify({"data": self.service.get_all()}), 200

    def one(self, id):
        return jsonify({"data": self.service.get_one(id)}), 200

    def del_one(self, id):
        self.service.del_one(id)
        return ('', 204)

    def del_many(self, list_of_ids):
        self.service.del_many(list_of_ids)
        return ('', 204)

    def create(self, data):
        return jsonify({"data": self.service.add_one(data)}), 201

    def create_many(self, data):
        return jsonify({"data": self.service.add_many(data)}), 201

    def update(self, id, data):
        return jsonify({"data": self.service.update_one(id, data)}), 200
