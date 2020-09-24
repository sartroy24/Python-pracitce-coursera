import json
data = '''[
    {
        "name":"Sarthak",
        "age":24
    },
    {
        "name":"Chris",
        "age":35
    }
]'''

info = json.loads(data)
print(len(info))
for item in info:
    print(item["name"])
    print(item["age"])