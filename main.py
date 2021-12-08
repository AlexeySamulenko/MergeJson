import argparse
from typing import List, Dict
from FileLoader import FileLoader
from FileWriter import WriterJSON, WriterXML
from SerializeXML import XMLSerializer


class MainTask:
    def __init__(self, argv):
        self.rooms = argv.rooms
        self.students = argv.students
        self.format = argv.format

    def run(self):
        loader = FileLoader()
        rooms_file = loader.load(self.rooms)
        students_file = loader.load(self.students)
        files_merged = self.merge(students_file, rooms_file)

        if self.format == 'json':
            writer = WriterJSON()
            writer.save(data=files_merged, path='merged', output_format='json')
        elif self.format == 'xml':
            xml = XMLSerializer()
            xml_data = xml.serialize(files_merged)
            writer = WriterXML()
            writer.save(data=xml_data, path="merged", output_format='xml')

    def merge(self, students, rooms) -> List[Dict]:
        for room in rooms:
            room['students'] = []
        for student in students:
            room_id: int = student['room']
            room: Dict = rooms[room_id]
            room['students'].append(student.get('id'))
        return rooms


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('students', type=str, help='path to students.json file')
    parser.add_argument('rooms', type=str, help='path to rooms.json file')
    parser.add_argument('format', type=str, choices=['json', 'xml'], help='output format options')
    args = parser.parse_args()
    MainTask(args).run()
