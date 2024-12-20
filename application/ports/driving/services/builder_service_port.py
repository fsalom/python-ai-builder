from abc import ABC, abstractmethod


class BuilderServicePort(ABC):

    @abstractmethod
    def create(self, json_input, tech):
        raise NotImplementedError
