from abc import ABC, abstractmethod

class notificationMethod(ABC):

    @abstractmethod
    def notify(self, message: str):
        pass
