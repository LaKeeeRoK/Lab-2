import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()

Name = []
Value = []

for valute in root.findall('Valute'):
    name = valute.find('Name').text
    value = valute.find('Value').text
    Name.append(name)
    Value.append(value)


for i in range(len(Name)):
    print(Name[i], Value[i])
