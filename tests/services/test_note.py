import pytest
from unittest.mock import MagicMock
from dao.models.note import Note
from dao.note_dao import NoteDAO
from services.note_service import NoteService


@pytest.fixture
def test_note_dao():
    test_dao = NoteDAO(None)

    sky_smart = Note(id=1, text="Sth about SkySmart")
    sky_eng = Note(id=1, text="Sth about SkyEng")
    sky_pro = Note(id=1, text="Sth about SkyPro")

    test_dao.get_one = MagicMock(return_value=sky_eng)
    test_dao.get_all = MagicMock(return_value=[sky_smart, sky_eng, sky_pro])
    test_dao.create = MagicMock(return_value=Note(id=3))
    test_dao.update = MagicMock(return_value=None)
    test_dao.delete = MagicMock(return_value=None)

    return test_dao


class TestNoteService:

    @pytest.fixture(autouse=True)
    def test_genre_service(self, test_note_dao):
        self.tns = NoteService(dao=test_note_dao)

    def test_get_one(self):
        note = self.tns.get_one(1)

        assert isinstance(note, Note)

    def test_get_all(self):
        notes = self.tns.get_all()

        assert len(notes) > 0
        assert isinstance(notes[0], Note)

    def test_create(self):
        data = {
            "text": "La la la"
        }
        note = self.tns.create(data)

        assert isinstance(note, Note)

    def test_update(self):
        data = {
            "name": "La la la"
        }
        self.tns.update(data, 1)
        note = self.tns.get_one(1)

        assert isinstance(note, Note)
        assert note.text == "La la la"

    def test_update_partial(self):
        data = {
            "name": "La la la"
        }
        self.tns.update(data, 2)
        note = self.tns.get_one(2)

        assert isinstance(note, Note)
        assert note.text == "La la la"

    def test_delete(self):
        note = self.tns.delete(1)

        assert note is None
