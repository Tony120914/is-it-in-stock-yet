import os
from datetime import datetime
import discordNotification

def check(soup):
    inStockButton = soup.find(id='js-productDetailBuyButton')
    innerText = inStockButton.getText(strip=True).lower()
    print(f'{datetime.now()} ||| Stock status: {innerText}')
    if innerText == 'add to cart':
        url = os.environ.get('URL')
        message = f'THE BIKE IS IN STOCK\n{url}\n(If I\'m still spamming and Tony isn\'t available to stop me, right click me on the sidebar and mute me for now.)'
        discordNotification.dmNotify(message)
