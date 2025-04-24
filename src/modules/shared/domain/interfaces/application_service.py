from abc import ABC, abstractmethod


class UseCase(ABC):
    @abstractmethod
    def process(self, *args, **kwargs):
        raise NotImplementedError
