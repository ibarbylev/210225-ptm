"""
Создайте декоратор, для определения среднего времени выполнения функции.
Количество повторов должно задаваться с помощью параметра декоратора.

@average_time(5)
def get_request(url):
    request = requests.get(url)
    return request


get_request('https://google.com')

Результат:
1: -- 1.446 seconds
2: -- 1.433 seconds
3: -- 1.120 seconds
4: -- 1.115 seconds
5: -- 1.345 seconds
Среднее время выполнения за 5 запуск(ов): 1.292 сек
"""


import requests
import time

def average_time(repeats=1):
    pass



@average_time(5)
def get_request(url):
    request = requests.get(url)
    return request


get_request('https://google.com')
