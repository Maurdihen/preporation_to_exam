from dao.models.birthday import Birthday


class BirthdayDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Birthday).get(bid)

    def get_all(self):
        return self.session.query(Birthday).all()

    def create(self, data):
        note = Birthday(**data)

        self.session.add(note)
        self.session.commit()

        return note

    def update(self, birthday):

        self.session.add(birthday)
        self.session.commit()

        return birthday

    def delete(self, bid):
        birthday = self.get_one(bid)

        self.session.delete(birthday)
        self.session.commit()
