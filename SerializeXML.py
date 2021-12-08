from xml.etree import ElementTree as ET
from xml.dom.minidom import parseString


class XMLSerializer:
    def serialize(self, serialize_data):
        root = ET.Element('rooms')
        for room_data in serialize_data:
            each_room = ET.SubElement(root, 'room')
            ET.SubElement(each_room, 'id').text = str(room_data.get('id'))
            ET.SubElement(each_room, 'name').text = room_data.get('name')
            students_data = ET.SubElement(each_room, 'students')

            for student in room_data.get('students'):
                ET.SubElement(students_data, 'student').text = str(student)
        ET.ElementTree(root)
        return parseString(ET.tostring(root)).toprettyxml(indent='   ')
