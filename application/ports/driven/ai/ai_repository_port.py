from abc import ABC, abstractmethod


class AIRepositoryPort(ABC):

    @abstractmethod
    def create(self, json_input, tech):
        raise NotImplementedError
