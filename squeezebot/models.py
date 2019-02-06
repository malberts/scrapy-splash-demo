import peewee
from peewee import SqliteDatabase


db = SqliteDatabase("tracks.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField()


class Tag(BaseModel):
    name = peewee.CharField()


class Track(BaseModel):
    title = peewee.CharField()
    date = peewee.DateTimeField()
    user = peewee.ForeignKeyField(User, backref="tracks")
    tag = peewee.ForeignKeyField(Tag, backref="tracks", null=True)
    likes = peewee.IntegerField()
    url = peewee.CharField()
