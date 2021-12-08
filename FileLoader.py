import json
from abc import ABC, abstractmethod


class LoadABC(ABC):
    @abstractmethod
    def load(self, path):
        pass


class FileLoader(LoadABC):
    def load(self, path: str):
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f'File not found {path}')
