import json

data = '{"var1":"harry", "var2":56}'
# print(data['var1'])

parsed = json.loads(data)
# print(parsed['var1'])
# print(type(parsed))

data2 = {
    "channel_name":"codewithharry",
    "cars":['bmw', 'audi', 'ferrari'],
    "fridge":('roti', 'daal'),
    "isbad":False
}

jscom = json.dumps(data2)
print(jscom)