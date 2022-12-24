
# file_ = open('../README.md')
# try:
#     lines = file_.readlines()
# finally:
#     file_.close()
#
#
# with open('../README.md') as file_:
#     lines = file_.readlines()
#
#
# print(lines)
#
#
# class MyResource:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         ...
#
#     def print_message(self):
#         print('Hello!')
#
#
# my_res = MyResource().__enter__()
# try:
#     my_res.print_message()
# finally:
#     my_res.__exit__()
#
# with MyResource() as my_res:
#     my_res.print_message()



class MyFileManager:
    def __init__(self, filename, mode='r', encoding='UTF-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.__fp = open(self.filename, mode=self.mode, encoding=self.encoding)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not all([exc_type, exc_val, exc_tb]):
            print(exc_type, type(exc_val), type(exc_tb), sep=', ')
            self.__fp.close()
        else:
            print('Error')



    def run_error(self):
        raise TypeError('This is a error')

    def normal(self):
        print('Hello')




with MyFileManager('/Users/tytar/PycharmProjects/python_basic/README.md') as fp:
    # fp.run_error()
    fp.normal()



with open('a.txt') as a_file, open('b.txt') as b_file, open('c.txt') as c_file:
    lines_a = a_file.readlines()
    lines_b = b_file.readlines()
    c_file.writelines([*lines_a, *lines_b])


with open('a.txt') as a_file:
    with open('b.txt') as b_file:
        with open('c.txt') as c_file:
            lines_a = a_file.readlines()
            lines_b = b_file.readlines()
            c_file.writelines([*lines_a, *lines_b])

def cell(_value=None):

    def get():
        return _value

    def set(value):
        nonlocal _value
        _value = value

    return get, set


get, set = cell(10)


with set(11):
    print(get())



import os

class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self._previous_path = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self._previous_path)







