from dao.models.birthday import Birthday


class BirthdayDAO:
    """
    DAO (Data Access Object) для работы с днями рождения.
    """

    def __init__(self, session):
        """
        Инициализация объекта DAO.

        Args:
            session: Сессия базы данных.
        """
        self.session = session

    def get_one(self, bid):
        """
        Получить информацию о дне рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            Birthday: Объект дня рождения.
        """
        return self.session.query(Birthday).get(bid)

    def get_all(self):
        """
        Получить все дни рождения.

        Returns:
            list: Список дней рождения.
        """
        return self.session.query(Birthday).all()

    def create(self, data):
        """
        Создать новый день рождения.

        Args:
            data (dict): Данные нового дня рождения.

        Returns:
            Birthday: Созданный объект дня рождения.
        """
        note = Birthday(**data)

        self.session.add(note)
        self.session.commit()

        return note

    def update(self, birthday):
        """
        Обновить информацию о дне рождения.

        Args:
            birthday (Birthday): Объект дня рождения для обновления.

        Returns:
            Birthday: Обновленный объект дня рождения.
        """
        self.session.add(birthday)
        self.session.commit()

        return birthday

    def delete(self, bid):
        """
        Удалить день рождения по его идентификатору.

        Args:
            bid (int): Идентификатор дня рождения.

        Returns:
            None
        """
        birthday = self.get_one(bid)

        self.session.delete(birthday)
        self.session.commit()
