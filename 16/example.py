import pathlib
"""
"a!bc1d test2test", "d!cb1a tset2tset"
"abs1", "sba1"
"123","123"
"""


def reverse_string(string_: str) -> str:
    if not isinstance(string_, str):
        raise TypeError(f'Got {type(string_)}, expected string')
    new_words = []
    for word in string_.split():
        new_word = []
        nonletters = []
        for index, char in enumerate(word):
            if char.isalpha():
                new_word.append(char)
            else:
                nonletters.append((index, char))
        new_word = new_word[::-1]
        for item in nonletters:
            new_word.insert(*item)
        new_words.append(''.join(new_word))
    return ' '.join(new_words)


def read_text_from_file(path: pathlib.Path) -> list:
    with open(path) as f:
        return f.readlines()


def write_text_into_file(path: pathlib.Path, text: str) -> None:
    with open(path, 'w') as f:
        f.writelines(text)


def reverse_text_from_file(input_path: str, reversed_filename: str ='reversed.txt'):
    if not isinstance(input_path, str):
        raise TypeError(f'Got {type(input_path)}, expected string')
    if not isinstance(reversed_filename, str):
        raise TypeError(f'Got {type(reversed_filename)}, expected string')
    path = pathlib.Path(input_path)
    reversed_lines = []
    lines = read_text_from_file(path)
    for text in lines:
        reversed_lines.append(reverse_string(text))
    new_path = path.absolute().parent
    write_text_into_file(new_path / reversed_filename, '\n'.join(reversed_lines))


if __name__ == '__main__':
    reverse_text_from_file('/Users/tytar/PycharmProjects/python_basic/16/text.txt')
    # cases = [
    #     ("a!bc1d test2test", "d!cb1a tset2tset"),
    #     ("abs1", "sba1"),
    #     ("123", "123")
    # ]
    # for passed_value, expected_value in cases:
    #     assert reverse_string(passed_value) == expected_value
    # reverse_string(123)
