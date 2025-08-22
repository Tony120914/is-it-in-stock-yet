from .store import store
from bs4 import BeautifulSoup

class canyonBicycles(store):

    def check(self, soup: BeautifulSoup) -> bool:
        inStockButton = soup.find(id='js-productDetailBuyButton')
        if (not inStockButton): return False
        innerText = inStockButton.getText(strip=True).lower()
        print(f'Stock status: {innerText}', flush=True)
        return innerText == 'add to cart'
