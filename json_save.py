import json

person = {
    "name": "Max",
    "age": 10,
    "phones": ["9111", "123142"]

    }
result = json.dumps(person)
print(result)
print(type(result))


qpwdi = [1, 2, 3]
result = json.dumps(qpwdi)
print(result)
print(type(result))


result = json.loads(result)
print(type(result))
