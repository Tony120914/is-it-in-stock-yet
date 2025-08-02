from .store import store

class bestBuy(store):

    def check(self, soup):
        inStockButton = soup.find(id='PRODUCT_AND_MOBILE_DETAILS_ID')
        innerText = inStockButton.getText().lower()
        isAvailable = 'sold out' not in innerText and 'not available' not in innerText
        print(f"In stock?: {isAvailable}", flush=True)
        return isAvailable
