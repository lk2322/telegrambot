from peewee import *
import datetime
db = SqliteDatabase('usr.db')


class UserName(Model):
    usr_id = CharField()
    first_name = CharField()
    last_name = CharField()
    username = CharField()
    date = TimestampField()

    class Meta:
        database = db  # This model uses the "people.db" database.


def add_name(usr_id, current_nameF, current_nameL, username):
    db.connect()
    user_names = UserName.select().where(UserName.usr_id == usr_id)
    if not (any(map((lambda nameF: nameF.first_name == current_nameF), user_names)) and
            any(map((lambda nameL: nameL.last_name == current_nameL), user_names)) and
            any(map((lambda user_name: user_name.username == username), user_names))):
        UserName.create(usr_id=usr_id, first_name=current_nameF, last_name=current_nameL,
                        username=username, date=datetime.datetime.now())
    db.close()


def give_names(usr_id):
    db.connect()
    first_name = ''
    last_name = ''
    names = []
    counter = 0
    user_names = UserName.select().where(
        UserName.usr_id == usr_id).order_by(UserName.date.desc())
    for name in user_names:
        counter += 1
        first_name = name.first_name
        last_name = name.last_name
        username = name.username
        names.append([first_name, last_name, username])
        if counter == 10:
            break
    db.close()
    return names
