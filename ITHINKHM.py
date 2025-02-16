import os

import requests
import random

a = os.listdir(r'C:\Users\user\PycharmProjects\openWeatherAPI\the kots')


def unique_path_generator():
    unique_number = ''
    for _ in range(99):
        unique_number += str(random.randint(0, 9))
    return r"C:\Users\user\PycharmProjects\openWeatherAPI\the kots\kot" + unique_number + '.jpg'


user_limit = int(input())
r = requests.get(f'https://api.thecatapi.com/v1/images/search?limit={user_limit}')
for i in range(user_limit):
    url = r.json()[i].get('url')
    hz = requests.get(url)
    with open(unique_path_generator(), 'wb+') as f:
        f.write(hz.content)
    user_limit -= 1
