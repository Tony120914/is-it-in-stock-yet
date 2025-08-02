from abc import ABC, abstractmethod

class store(ABC):

    @abstractmethod
    def check(self, soup):
        pass
