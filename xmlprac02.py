import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>01</id>
            <name>Sarthak</name>
        </user>
        <user x="7">
            <id>02</id>
            <name>Chris</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Name', item.find('id').text)
    print('Name', item.get('x'))