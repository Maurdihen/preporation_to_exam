from datetime import datetime

from dao.birthday_dao import BirthdayDAO


class BirthdayService:

    def __init__(self, dao: BirthdayDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["birthday_date"] = datetime.strptime(data["birthday_date"], '%Y-%m-%d').date()
        return self.dao.create(data)

    def update(self, data, bid):
        birthday = self.dao.get_one(bid)
        data["birthday_date"] = datetime.strptime(data["birthday_date"], '%Y-%m-%d').date()

        birthday.full_name = data.get("full_name")
        birthday.birthday_date = data.get("birthday_date")
        birthday.present = data.get("present")

        self.dao.update(birthday)

    def update_partial(self, data, bid):
        birthday = self.get_one(bid)

        if "full_name" in data:
            birthday.full_name = data.get("full_name")

        if "birthday_date" in data:
            data["birthday_date"] = datetime.strptime(data["birthday_date"], '%Y-%m-%d').date()
            birthday.birthday_date = data.get("birthday_date")

        if "present" in data:
            birthday.present = data.get("present")

        self.dao.update(birthday)

    def delete(self, bid):
        return self.dao.delete(bid)
