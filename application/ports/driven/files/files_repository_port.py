from abc import ABC, abstractmethod
from typing import List
from domain.directory import Directory


class FilesRepositoryPort(ABC):

    @abstractmethod
    def read_file(self, path, extensions: [str]) -> str:
        raise NotImplementedError

    @abstractmethod
    def read_dir(self, path) -> List[Directory]:
        raise NotImplementedError
