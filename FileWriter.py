import json
from abc import ABC, abstractmethod


class WriterABC(ABC):
    @abstractmethod
    def save(self, data, path, output_format):
        pass


class WriterJSON(WriterABC):
    def save(self, data, path, output_format):
        with open(f'{path}.{output_format}', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)


class WriterXML(WriterABC):
    def save(self, data, path, output_format):
        with open(f'{path}.{output_format}', 'w', encoding='utf-8') as f:
            f.write(str(data))
