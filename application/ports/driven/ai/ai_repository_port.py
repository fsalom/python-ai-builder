from abc import ABC, abstractmethod


class AIRepositoryPort(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError
