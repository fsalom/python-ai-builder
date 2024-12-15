from abc import ABC, abstractmethod


class BuilderServicePort(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError
