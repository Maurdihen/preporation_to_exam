from datetime import datetime

from dao.birthday_dao import BirthdayDAO


class BirthdayService:
    """
    Сервис для работы с днями рождения.
    """

    def __init__(self, dao: BirthdayDAO):
        """
        Инициализация объекта сервиса.

        Args:
            dao (BirthdayDAO): DAO для работы с днями рождения.
        """
        self.dao = dao

    def get_one(self, bid):
        """
        Получить информацию о дне рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            Birthday: Объект дня рождения.
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Получить все дни рождения.

        Returns:
            list: Список дней рождения.
        """
        return self.dao.get_all()

    def create(self, data):
        """
        Создать новый день рождения.

        Args:
            data (dict): Данные нового дня рождения.

        Returns:
            Birthday: Созданный объект дня рождения.
        """
        data["birthday_date"] = datetime.strptime(data["birthday_date"], '%Y-%m-%d').date()
        return self.dao.create(data)

    def update(self, data, bid):
        """
        Обновить информацию о дне рождения по его идентификатору.

        Args:
            data (dict): Обновленные данные дня рождения.
            bid (int): Идентификатор дня рождения.

        Returns:
            None
        """
        birthday = self.dao.get_one(bid)
        data["birthday_date"] = datetime.strptime(data["birthday_date"], '%Y-%m-%d').date()

        birthday.full_name = data.get("full_name")
        birthday.birthday_date = data.get("birthday_date")
        birthday.present = data.get("present")

        self.dao.update(birthday)

    def update_partial(self, data, bid):
        """
        Частично обновить информацию о дне рождения по его идентификатору.

        Args:
            data (dict): Частично обновленные данные дня рождения.
            bid (int): Идентификатор дня рождения.

        Returns:
            None
        """
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
        """
        Удалить день рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            None
        """
        return self.dao.delete(bid)
