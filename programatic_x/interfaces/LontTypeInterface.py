from abc import ABC, abstractmethod

class LontTypeInterface(ABC):
    @abstractmethod
    def type(self, text: str):
        pass
