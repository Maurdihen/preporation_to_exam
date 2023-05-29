from dao.models.note import Note


class NoteDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, nid):
        return self.session.query(Note).get(nid)

    def get_all(self):
        return self.session.query(Note).all()

    def create(self, data):
        note = Note(**data)

        self.session.add(note)
        self.session.commit()

        return note

    def update(self, note):

        self.session.add(note)
        self.session.commit()

        return note

    def delete(self, nid):
        note = self.get_one(nid)

        self.session.delete(note)
        self.session.commit()
