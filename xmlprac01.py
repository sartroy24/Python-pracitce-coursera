import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 23456 9022
    </phone>
    <email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Email:',tree.find('email').find('hide'))
