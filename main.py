import importlib
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from notificationMethods.notificationMethod import notificationMethod
from stores.store import store
from threading import Timer

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
    load_dotenv()
    interval = float(os.environ.get('INTERVAL') or 60)
    notifMethodName = os.environ.get('NOTIFICATION_METHOD') or 'alert'
    try:
        itemUrl = os.environ['ITEM_URL']
        storeName = os.environ['STORE']
        userAgent = os.environ['USER_AGENT']
    except Exception as e:
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
