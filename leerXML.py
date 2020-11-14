import xml.etree.ElementTree as ET

tree = ET.parse('archivo_xml_Ev3.xml')
root = tree.getroot()
for child in root:
   print (child.tag, child.attrib)

#---Resultado
# empleado {'id': '1'}
# empleado {'id': '2'}