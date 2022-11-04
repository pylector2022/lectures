res = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5', 'key_6': 'value_6' , 'key_7': 'value_7', 'key_8': 'value_8', 'key_9': 'value_9', 'key_10': 'value_10'}

res_1 = {}
for key, val in res.items():
    number = int(key.split('_')[-1])
    if number % 2 != 0:
        res_1[key] = val
        res_1.update({key: val})


res = {'key_1': 'value_1', 'key_3': 'value_3', 'key_5': 'value_5', 'key_7': 'value_7', 'key_9': 'value_9', 'key_11': 'value_11' }


dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}


dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}


set_a = set(dict_a.items())
set_b = set(dict_b.items())
set_c = set(dict_c.items())
res = {
    'dict_a': len(set_a & set_c),
    'dict_b': len(set_b & set_c)
}
print(f'res = {res}')


keys = dict_a.keys()
values = dict_b.values()
res = dict(zip(keys, values))
res = {key: value for key, value in zip(dict_a.keys(), dict_b.values())}
{key, value}
dict(zip(keys, values))
{}
dict()
