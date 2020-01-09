import json
import xmltodict 
 
with open('complexes.json', 'r', encoding='UTF-8') as f:
    jsonString = f.read()
 
print('JSON input (json_to_xml.json):')
print(jsonString)
 
xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
   
print('\nXML output(json_to_xml.xml):')
print(xmlString)
   
with open('json_to_xml.xml', 'w') as f:
    f.write(xmlString)