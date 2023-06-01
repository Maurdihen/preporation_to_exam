from flask import request
from flask_restx import Resource, Namespace

from dao.models.birthday import BirthdaysSchema
from implemented import birthday_service


birthday_ns = Namespace('birthday')

birthday_schema = BirthdaysSchema()
birthdays_schema = BirthdaysSchema(many=True)

@birthday_ns.route('/')
class NotesView(Resource):

    def get(self):
        birthdays = birthday_service.get_all()
        # return birthdays_schema.dump(birthdays), 200
        return "hello"

    def post(self):
        data = request.json
        birthday_service.create(data)

        return "OK", 201


@birthday_ns.route('/<int:bid>')
class NoteView(Resource):

    def get(self, bid):
        birthday = birthday_service.get_one(bid)
        return birthday_schema.dump(birthday), 200

    def put(self, bid):
        data = request.json
        birthday_service.update(data, bid)

        return "OK", 204

    def patch(self, bid):
        data = request.json
        birthday_service.update_partial(data, bid)

        return "OK", 204

    def delete(self, bid):
        birthday_service.delete(bid)
        return "OK", 204
