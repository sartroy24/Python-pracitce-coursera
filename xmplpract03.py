import xml.etree.ElementTree as ET
input = '''<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <price>29.99</price>
</book>
<book>
  <title lang="en">Learning XML</title>
  <price>39.95</price>
</book>
</bookstore>'''
stuff = ET.fromstring(input)
lst = stuff.findall('.//book')
for i in lst:
    print(i.find('price').text)
    # print('Name', item.find('name').text)
    # print('Name', item.find('id').text)
    # print('Name', item.get('x'))
