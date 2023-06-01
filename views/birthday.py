from flask import request
from flask_restx import Resource, Namespace

from dao.models.birthday import BirthdaysSchema
from implemented import birthday_service

birthday_ns = Namespace('birthday')

birthday_schema = BirthdaysSchema()
birthdays_schema = BirthdaysSchema(many=True)

@birthday_ns.route('/')
class NotesView(Resource):
    """
    Ресурс для работы с днями рождения.

    Работает с коллекцией дней рождения.
    """

    def get(self):
        """
        Получить все дни рождения.

        Returns:
            tuple: Список дней рождения и код состояния HTTP 200.
        """
        birthdays = birthday_service.get_all()
        return birthdays_schema.dump(birthdays), 200

    def post(self):
        """
        Создать новый день рождения.

        Returns:
            tuple: Сообщение об успешном создании и код состояния HTTP 201.
        """
        data = request.json
        birthday_service.create(data)

        return "OK", 201


@birthday_ns.route('/<int:bid>')
class NoteView(Resource):
    """
    Ресурс для работы с конкретным днем рождения.

    Работает с отдельным днем рождения по его идентификатору.
    """

    def get(self, bid):
        """
        Получить информацию о дне рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            tuple: Информация о дне рождения и код состояния HTTP 200.
        """
        birthday = birthday_service.get_one(bid)
        return birthday_schema.dump(birthday), 200

    def put(self, bid):
        """
        Обновить информацию о дне рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            tuple: Сообщение об успешном обновлении и код состояния HTTP 204.
        """
        data = request.json
        birthday_service.update(data, bid)

        return "OK", 204

    def patch(self, bid):
        """
        Частично обновить информацию о дне рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            tuple: Сообщение об успешном обновлении и код состояния HTTP 204.
        """
        data = request.json
        birthday_service.update_partial(data, bid)

        return "OK", 204

    def delete(self, bid):
        """
        Удалить день рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            tuple: Сообщение об успешном удалении и код состояния HTTP 204.
        """
        birthday_service.delete(bid)
        return "OK", 204
