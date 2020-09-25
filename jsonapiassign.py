import urllib.request, urllib.parse, urllib.error
import json

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_972261.json')
data = fhand.read().decode()
info = json.loads(data)
total = 0
for item in info["comments"]:
    total = total + item["count"]
print(total)