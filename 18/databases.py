import pprint
from playhouse.shortcuts import model_to_dict

"""
SQL -> MySQL, SQLite, PostgreSQL, MariaDb ...
NoSQL ->
      -key:value-storage - Redis
      -document oriented database - Mongo



author 
   -> book1
   -> book2

1 - oo
1 - 1
oo - oo

1. ORM
2. sql

# Table Crew
id  | crew_id  | Name
-----------------------
1  |  E998THD  | John Dou
2  |  E998THD  | John Snow


# Enter
id  | person_id | date time
------------------------------------
123 |    1      | 12.12.2012 12:12:12
123 |    1      | 12.12.2012 12:12:12
123 |    1      | 12.12.2012 12:12:12


# Exit
id  | person_id | date time
------------------------------------
123 |    1      | 12.12.2012 12:12:12
123 |    1      | 12.12.2012 12:12:12
123 |    1      | 12.12.2012 12:12:12
123 |    1      | 12.12.2012 12:12:12

"""

from peewee import *

db = SqliteDatabase('people.db')


class BaseModel(Model):
    class Meta:
        database = db


class PersonModel(BaseModel):
    crew_id = CharField()
    name = CharField()


class EnterModel(BaseModel):
    person = ForeignKeyField(PersonModel)
    datetime = CharField()


class ExitModel(BaseModel):
    person = ForeignKeyField(PersonModel)
    datetime = CharField()


if __name__ == '__main__':
    """
    your package should be version 1.0.2
    """
    db.connect()
    db.create_tables([PersonModel, EnterModel, ExitModel])

    # person = {
    #     'crew_id': 'E998THD',
    #     'name': 'John Dou'
    # }

    # person_obj = PersonModel.create(**person)
    #
    # enter_obj = EnterModel.create(person=person_obj, datetime='12:23:23 12.12.2012')
    # exit_obj = ExitModel.create(person=person_obj, datetime='12:23:23 12.12.2012')

    # persons = PersonModel.select().where(PersonModel.crew_id == 'E998THD')
    #
    # for person_obj in persons:
    #     pprint.pprint(model_to_dict(person_obj))
    #
    #     dates = ExitModel.select().where(ExitModel.person_id == person_obj.id)
    #     for date in person_obj.exitmodel_set.select():
    #         pprint.pprint(model_to_dict(date))

    with my_db.atomic():
        crew, enter, exit = read_files()
        for person in crew:
            person_dict = parse_crew(person)
            person_obj = PersonModel.create(**person)

            for item in enter:
                date_time_dict = parse_datetime(item)
                if date_time_dict.get('crew_id') == person_dict.get('crew_id'):
                    EnterModel.create(person=person_obj, datetime=date_time_dict.get('datetime'))

            for item in exit:
                date_time_dict = parse_datetime(item)
                if date_time_dict.get('crew_id') == person_dict.get('crew_id'):
                    ExitModel.create(person=person_obj, datetime=date_time_dict.get('datetime'))

    db.close()
"""

SELECT pm.*, exm.datetime as exit_time, emm.datetime as enter_time 
FROM `personmodel` as pm
JOIN `exitmodel` as exm ON exm.person_id = pm.id
JOIN `entermodel` as emm ON emm.person_id = pm.id
WHERE pm.crew_id = "E998THD"

"""