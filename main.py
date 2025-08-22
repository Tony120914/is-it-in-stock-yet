import os
import importlib
import requests
from bs4 import BeautifulSoup
from threading import Timer
from stores.store import store
from notificationMethods.notificationMethod import notificationMethod

'''
    Repeatly checks the online store for stock every interval.
'''
def repeat(interval: float, itemUrl: str, headers: dict[str, str], store: store, notifMethod: notificationMethod):
    timer = Timer(interval, repeat, (interval, itemUrl, headers, store, notifMethod))
    timer.start()

    timeout = 30
    try:
        response = requests.get(itemUrl, headers=headers, timeout=timeout)
        soup = BeautifulSoup(response.text, features='html.parser')
        inStock = store.check(soup)
        if (inStock):
            message = f'THE ITEM IS IN STOCK!\n{itemUrl}'
            notifMethod.notify(message)
            timer.cancel()
    except requests.exceptions.RequestException as e:
        print(f'Store check failed:\n{e}')

def main():
    interval = float(os.environ.get('INTERVAL') or 60)
    notifMethodName = os.environ.get('NOTIFICATION_METHOD') or 'alert'
    try:
        itemUrl = os.environ.get('ITEM_URL') or ''
        storeName = os.environ.get('STORE') or ''
        userAgent = os.environ.get('USER_AGENT') or ''
        if (not all((itemUrl, storeName, userAgent))): raise NameError('At least one required .env variable is missing')
    except NameError as e:
        print(f'.env file is not populated correctly, refer to .env.template:\n{e}')
        return

    try:
        storeModule = importlib.import_module(f"stores.{storeName}")
        store = getattr(storeModule, storeName)()
        notifMethodModule = importlib.import_module(f"notificationMethods.{notifMethodName}")
        notifMethod = getattr(notifMethodModule, notifMethodName)()
    except Exception as e:
        print(f'Invalid store or notification method:\n{e}')
        return
    
    headers = {'User-Agent': userAgent}
    repeat(interval, itemUrl, headers, store, notifMethod)

if __name__ == "__main__":
    main()
