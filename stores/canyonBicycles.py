import os
import discordNotification

def check(soup):
    inStockButton = soup.find(id='js-productDetailBuyButton')
    innerText = inStockButton.getText(strip=True).lower()
    print(f'Stock status: {innerText}', flush=True)
    if innerText == 'add to cart':
        url = os.environ.get('ITEM_URL')
        message = f'THE BIKE IS IN STOCK\n{url}\n(If I\'m still spamming and Tony isn\'t available to stop me, right click me on the sidebar and mute me for now.)'
        discordNotification.dmNotify(message)
