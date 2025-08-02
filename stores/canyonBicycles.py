from .store import store

class canyonBicycles(store):

    def check(self, soup):
        inStockButton = soup.find(id='js-productDetailBuyButton')
        innerText = inStockButton.getText(strip=True).lower()
        print(f'Stock status: {innerText}', flush=True)
        return innerText == 'add to cart'
