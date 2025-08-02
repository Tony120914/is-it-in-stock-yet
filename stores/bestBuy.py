from .store import store

class bestBuy(store):

    def check(self, soup):
        productDetails = soup.find(id='PRODUCT_AND_MOBILE_DETAILS_ID')
        innerText = productDetails.getText().lower()
        isAvailable = 'sold out' not in innerText
        print(f"In stock?: {isAvailable}", flush=True)
        return isAvailable
