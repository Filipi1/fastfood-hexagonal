from abc import ABC, abstractmethod


class DomainService(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError("DomainService must implement execute method")
