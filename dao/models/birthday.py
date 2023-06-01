from setup_db import db
from marshmallow import Schema, fields

class Birthday(db.Model):
    __tablename__ = 'birthday'

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100))
    birthday_date = db.Column(db.Date)
    present = db.Column(db.String(1000))


class BirthdaysSchema(Schema):
    id = fields.Int(dump_only=True)
    full_name = fields.Str()
    birthday_date = fields.DateTime(dump_only=True)
    present = fields.Str()
