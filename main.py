import requests

data = set()
while len(data) != 16:
    data.add(tuple(map(tuple, requests.get("https://olimp.miet.ru/ppo_it/api").json()['message']['data'])))
print(data)
