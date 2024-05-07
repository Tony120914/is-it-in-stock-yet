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

'''
    Dummy app for port binding
'''
def app(environ, start_response):
    data = b'hi\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

if __name__ == '__main__':
    url = os.environ.get('URL')
    headers = {'User-Agent': os.environ.get('USER_AGENT')}
    store = eval(os.environ.get('STORE'))
    interval = float(os.environ.get('INTERVAL'))
    
    repeat(url, headers, store, interval)
