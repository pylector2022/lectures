from flask import Flask, render_template, abort
from peewee import *
from pprint import pp

DB_NAME = 'people.db'

app = Flask(__name__)
db = SqliteDatabase(DB_NAME)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class PersonModel(BaseModel):
    crew_id = CharField()
    name = CharField()

    # enter = EnterModel.where(person_id = PersonModel.id)


class EnterModel(BaseModel):
    person = ForeignKeyField(PersonModel, backref='enter')
    datetime = CharField()


class ExitModel(BaseModel):
    person = ForeignKeyField(PersonModel)
    datetime = CharField()


# url
@app.route('/persons/')
def index():
    persons = [person for person in PersonModel.select()]
    return render_template('persons.html', persons=persons)


@app.route('/persons/<person_id>')
def person_date_info(person_id):
    res = PersonModel.select().where(PersonModel.id == person_id)
    if len(res) != 1:
        abort(404)
    person = res[0]
    enters = EnterModel.select().where(EnterModel.person == person.id)
    exits = ExitModel.select().where(EnterModel.person == person.id)
    visits = your_func(enters, exits)  # [(enter_datetime, exit_datetime), (...],
    person_ = {
        'name': person.name,
        'crew_id': person.crew_id,
        'visits': visits
    }
    pp(person_)
    return render_template('person_profile.html', person=person_)
