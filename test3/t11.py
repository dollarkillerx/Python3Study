# import json

# json_str = '{"name":"dollarkiller","age":18}'

# student = json.loads(json_str)

# print(student)

# print(type(student))


import json

student = [
    {
        'name':'qiyue',
        'age':18,
        'flag':False
    },
    {
        'name':'dollarkiller',
        'age':20
    }
]

json_str = json.dumps(student)

print(json_str)