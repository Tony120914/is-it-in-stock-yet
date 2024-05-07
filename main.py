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

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    keepInstanceAwake()
    store.check(soup)

'''
    Keep free tier instance awake by periodically calling this function
'''
def keepInstanceAwake():
    url = os.environ.get('RENDER_URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    response = requests.get(url, headers=headers)
    print(f'This instance\'s status code: {response.status_code}')


def main():
    url = os.environ.get('URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    store = eval(os.environ.get('STORE'))
    interval = float(os.environ.get('INTERVAL'))
    
    repeat(url, headers, store, interval)

main()
