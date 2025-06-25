"""
Создайте декоратор, определяющий время выполнения функции.

@timeer
def get_request(url):
    request = requests.get(url)
    return request


get_request('https://google.com')

Результат:
Время выполнения функции get_request: 1.212 seconds
"""


import requests
import time

def timer(func):
    pass


@timer
def get_request(url):
    request = requests.get(url)
    return request


get_request('https://google.com')
