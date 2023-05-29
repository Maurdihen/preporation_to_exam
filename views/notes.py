from flask import request
from flask_restx import Resource, Namespace
from dao.models.note import NoteSchema
from implemented import note_service


note_ns = Namespace('notes')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


@note_ns.route('/')
class NotesView(Resource):

    def get(self):
        notes = note_service.get_all()
        return notes_schema.dump(notes), 200

    def post(self):
        data = request.json
        note_service.create(data)

        return "OK", 201


@note_ns.route('/<int:nid>')
class NoteView(Resource):

    def get(self, nid):
        note = note_service.get_one(nid)
        return note_schema.dump(note), 200

    def put(self, nid):
        data = request.json
        note_service.update(data, nid)

        return "OK", 204

    def patch(self, nid):
        data = request.json
        note_service.update_partial(data, nid)

        return "OK", 204

    def delete(self, nid):
        note_service.delete(nid)
        return "OK", 204
