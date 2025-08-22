from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class store(ABC):

    @abstractmethod
    def check(self, soup: BeautifulSoup) -> bool:
        pass
