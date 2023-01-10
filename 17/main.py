from flask import Flask, request
import example

app = Flask(__name__)
PATH = './data'


# url
@app.route('/persons/')
def index(person_id):
    res = example.get_person_data(person_id, PATH)
    return f"{res}"


@app.route('/person2/<person_id>/dates/<date_time>')
def person_date_info(person_id, date_time):
    return f"{person_id, date_time}, {request.method == 'get'}"
