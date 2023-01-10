import time, random, string

PORT_FILE = './port_8080'
RESPONSE_FILE = './response'


def generate_id(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.sample(chars, size))


def main(port=PORT_FILE):
    prev_url = None
    while 1:
        with open(port) as rfp:
            url = rfp.readline()
            if url != prev_url:
                if url.startswith('/persons/'):
                    data = index('some_id')
                    with open(RESPONSE_FILE, 'w+') as wfp:
                        wfp.write(data)
                prev_url = url
        time.sleep(1)


async def get_data_from_db(person_id):
    time.sleep(20)
    return generate_id()


def crop_photo():
    pass


def colored_photo():
    pass


def index(person_id):
    person_data = get_data_from_db(person_id)  # 20 sec
    photo = get_data_from_db(person_id)  # 10 sec
    ...
    crop_photo(photo)
    colored_photo(photo)
    return f'<h1>This is a string, {person_data=} {photo=}</h1>'


if __name__ == '__main__':
    main()
"""

thread1 -task1-------------------------
thread2 -------task2-------------------
thread3 -------------task3-------------

async   -task1task2task3-------task3------task1---task2--return
          
           



"""










