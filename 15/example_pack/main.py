"""
example
res = {
    '052XL7D4': {
        'name': 'БОЙКО ВОЛОДИМИР ІВАНОВИЧ'
        'visits': {
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ],
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ]
        }
    },

    '052XL7D4': {
        'name': 'БОЙКО ВОЛОДИМИР ІВАНОВИЧ'
        'visits': {
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ],
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ]
        }
    },

    ...
}

"""

PATH = '<your_filepath>'

CREW_FILENAME = 'crew.txt'
ENTRANCE_FILENAME = 'entrance.log'
EXIT_FILENAME = 'exit.log'


def read_files(path: str) -> tuple:
    # pathlib
    path = ...
    with open(path / CREW_FILENAME) as cf, \
        open(path / ENTRANCE_FILENAME) as enf, \
        open(path / EXIT_FILENAME) as exf:
        crew = cf.readlines()
        enter = enf.readlines()
        exit = exf.readlines()
    return crew, enter, exit


def main(path: str, ) -> list:
    return []


if __name__ == '__main__':
    from pprint import pprint
    pprint(main(PATH), width=100)
