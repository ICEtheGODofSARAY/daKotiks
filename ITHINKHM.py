import requests
import random


def unique_path_generator():
    chisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    base_path = r"C:\Users\user\PycharmProjects\openWeatherAPI\the kots\kot"
    unique_number = ''
    for _ in range(1, 100):
        unique_number += str(random.choice(chisla))
    full_path = base_path + str(unique_number) + '.jpg'
    return full_path


user_limit = int(input())
r = requests.get(f'https://api.thecatapi.com/v1/images/search?limit={user_limit}')
for i in range(user_limit):
    url = r.json()[i].get('url')
    hz = requests.get(url)
    with open(unique_path_generator(), 'wb+') as f:
        f.write(hz.content)
    user_limit -= 1
