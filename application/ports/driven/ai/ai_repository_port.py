from abc import ABC, abstractmethod


class AIRepositoryPort(ABC):

    @abstractmethod
    def create(self, json_input):
        raise NotImplementedError
