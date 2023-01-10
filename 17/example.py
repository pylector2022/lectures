"""

github
main/master
    -> commit_hash1 -> base func -> tag -> 1.0.1
    -> commit_hash2 -> extend func -> tag -> 1.0.2





secure_system ->  [   gap   ]  -> telegram-bot
 |
 Y
 read files
   crew.txt
   enter.txt
   exit.txt

web site
                                                                         ->052XL7D4
1. Request: browser -> [ internet ] -> server -> site -> get_person_data(person_id, data=None)
2. Response: get_person_data(person_id, date) -> site -> server -> [ internet ] -> browser


1. input person_id = 052XL7D4, date
2. res = get_person_data(person_id, data=None)
3. return res



"""


class Request(dict):
    ...


class Response:
    def render(self, template: str, data: dict) -> str:
        return ''


class View:


    def send(self, *args):
        ...

request = Request()
response = Response()

view = View()

import dataclasses


@dataclasses.dataclass()
class PersonModel:
    id = IDType()
    name = NameType()


@dataclasses.dataclass()
class EnterDateModel:
    person = IDExtendedType(PersonModel)
    datetime = DateTimeType()


# ORM
datetime1 = EnterDateModel(**date)
datetime1.datetime
datetime.person.id
datetime.person.name


def get_person_data(person_id: str, date: [str, None] = None) -> dict:
    person_data = get_person_from_file(person_id)  # {'person_id': 'XXXXX', 'name': 'Name'
    person_obj = PersonModel(**person_data)
    if date:
        person_data = get_data_from_file(person_id, date)
        person_data_list = [EnterDateModel(**date) for date in person_data]
    return {'person': person_obj, 'dates': person_data_list}


def valid_person_id(person_id) -> bool:
    """
    XXXXXXXX [0-9A-Z]
    :param person_id:
    :return:
    """
    return True


def valid_date(date: str) -> bool:
    """
    XXXX-XX-XX XX:XX:XX
    :param date:
    :return:
    """
    return True


def controller():
    person_id = request.get('person_id')
    if not valid_person_id(person_id):
        raise Exception()
    date = request.get('date')
    if not valid_date(date):
        raise Exception()
    person_data = get_person_data(person_id, date)
    rendered_template = response.render('./templates/person_profile.html', person_data)
    return rendered_template







if __name__ == '__main__':
    view.send(controller())
