import os
import requests
from bs4 import BeautifulSoup
from threading import Timer
import canyonBicycles

'''
    Repeatly checks the online store for stock every interval.
'''
def repeat(url, headers, store, interval):
    timer = Timer(interval, repeat, (url, headers, store, interval))
    timer.start()

    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, features='html.parser')
    store.check(soup)

def main():
    url = os.environ.get('URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    store = eval(os.environ.get('STORE'))
    interval = float(os.environ.get('INTERVAL'))
    
    repeat(url, headers, store, interval)

main()
