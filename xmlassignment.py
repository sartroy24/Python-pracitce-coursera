import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_972260.xml')
data = fhand.read().decode()
print(data)
tree = ET.fromstring(data)
lst = tree.findall('commentinfo/comments/comment')
sum = 0
print(len(lst))
for item in lst:
    sum = sum + int(item.text)
print(sum)