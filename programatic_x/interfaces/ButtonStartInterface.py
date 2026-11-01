from abc import ABC, abstractmethod

class ButtonStartInterface(ABC):
    @abstractmethod
    def click(self):
        pass