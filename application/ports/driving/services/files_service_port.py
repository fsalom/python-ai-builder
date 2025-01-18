from abc import ABC, abstractmethod


class FilesServicePort(ABC):

    @abstractmethod
    def read_dir(self, path):
        raise NotImplementedError
