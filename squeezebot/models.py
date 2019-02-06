import peewee
from peewee import SqliteDatabase


db = SqliteDatabase("tracks.db")


class Track(peewee.Model):
    title = peewee.CharField()
    date = peewee.DateTimeField()
    user = peewee.CharField()
    tag = peewee.CharField()
    likes = peewee.IntegerField()
    url = peewee.CharField()

    class Meta:
        database = db
