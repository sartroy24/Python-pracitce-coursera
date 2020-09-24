import json
data = '''{
    "name":"Sarthak",
    "phone":{
        "type":"integer",
        "number":9093086421
    },
    "email":{
        "hide":"yes"
    }
}'''

info = json.loads(data)
print('Name : ', info["name"])
print('Email hide: ', info["email"]["hide"])