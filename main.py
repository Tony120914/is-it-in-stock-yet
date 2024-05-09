import os
import requests
from bs4 import BeautifulSoup
from threading import Timer
import stores.canyonBicycles as canyonBicycles

'''
    Repeatly checks the online store for stock every interval.
'''
def repeat(url, headers, store, interval):
    timer = Timer(interval, repeat, (url, headers, store, interval))
    timer.start()

    keepInstanceAwake()
    timeout = 5
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        soup = BeautifulSoup(response.text, features='html.parser')
        store.check(soup)
    except:
        print(f'Store check failed by hanging after {timeout} seconds or incorrectly parsed')

    
        

'''
    Keep free tier instance awake by periodically calling this function
'''
def keepInstanceAwake():
    url = os.environ.get('RENDER_URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    timeout = 5
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        print(f'This instance\'s status code: {response.status_code}')
    except:
        print(f'Host server hung after {timeout} seconds')


def main():
    url = os.environ.get('URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    store = eval(os.environ.get('STORE'))
    interval = float(os.environ.get('INTERVAL'))
    
    repeat(url, headers, store, interval)

main()
