import os
import importlib
import requests
from bs4 import BeautifulSoup
from threading import Timer

'''
    Repeatly checks the online store for stock every interval.
'''
def repeat(store, url, interval, headers, notifMethod):
    timer = Timer(interval, repeat, (store, url, interval, headers, notifMethod))
    timer.start()

    timeout = 10
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        soup = BeautifulSoup(response.text, features='html.parser')
        inStock = store.check(soup)
        if (inStock):
            message = f'THE ITEM IS IN STOCK!\n{url}'
            notifMethod.notify(message)
            timer.cancel()
    except requests.exceptions.RequestException as e:
        print(f'Store check failed:\n{e}')

def main():
    storeModule = importlib.import_module(f"stores.{os.environ.get('STORE')}")
    store = getattr(storeModule, os.environ.get('STORE'))
    store = store()
    url = os.environ.get('ITEM_URL')
    interval = float(os.environ.get('INTERVAL'))
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    notifMethodModule = importlib.import_module(f"notificationMethods.{os.environ.get('NOTIFICATION_METHOD')}")
    notifMethod = getattr(notifMethodModule, os.environ.get('NOTIFICATION_METHOD'))
    notifMethod = notifMethod()
    
    repeat(store, url, interval, headers, notifMethod)

if __name__ == "__main__":
    main()
