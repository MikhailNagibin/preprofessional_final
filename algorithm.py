import numpy as np


def is_angels(data):
    tail = np.array(data)
    if np.array_equal(tail[0], np.array([255] * 64)) and np.array_equal(tail[1], [255] * 64)\
            and np.array_equal(tail[2], [255] * 64):
        if (np.array_equal(tail[::, 0].reshape(1, -1)[0], np.array([255] * 64))
                and np.array_equal(tail[:, 1].reshape(1, -1)[0], [255] * 64)
                and np.array_equal(tail[:, 2].reshape(1, -1)[0], [255] * 64)):
            return 1
        if (np.array_equal(tail[::, -1].reshape(1, -1)[0], np.array([255] * 64))
                and np.array_equal(tail[:, -2].reshape(1, -1)[0], [255] * 64)
                and np.array_equal(tail[:, -3].reshape(1, -1)[0], [255] * 64)):
            return 4
    if np.array_equal(tail[-1], [255] * 64) and np.array_equal(tail[-2], [255] * 64)\
            and np.array_equal(tail[-3], [255] * 64):
        if np.array_equal(tail[::, -1].reshape(1, -1)[0], [255] * 64):
          return 16
        if np.array_equal(tail[::, 0].reshape(1, -1)[0], [255] * 64):
            return 13
    return -1

def f23(data1, data13, data4, data16, curdata):
    tail = np.array(curdata)
    if np.array_equal(tail[0], [255] * 64):
        a = data1[:, -1] - tail[:, 0]
        b = data4[:, 0] - tail[:, -1]
        if sum(a) > sum(b):
            return 3
        else: return 2

        c = data13[:, -1] - tail[:, 0]
        d = data16[:, 0] - tail[:, -1]
        if sum(c) > sum(d):
            return 15
        else:
            return 14

def f59(data1, data13, data4, data16, curdata):
    tail = np.array(curdata)
    if np.array_equal(tail[0], [255] * 64):
        a = data1[:, -1] - tail[:, 0]
        b = data13[:, 0] - tail[:, -1]
        if sum(a) > sum(b):
            return 9
        else: return 5

        c = data4[:, -1] - tail[:, 0]
        d = data16[:, 0] - tail[:, -1]
        if sum(c) > sum(d):
            return 12
        else: return 8


import numpy as np
import requests
# from algorithm import *
from our_requests import *
import numpy as np
# data = requests.get('https://olimp.miet.ru/ppo_it/api').json()['message']['data']
# # print(*requests.get('https://olimp.miet.ru/ppo_it/api').json()['message']['data'], sep='\n')
#
# print(len(data[0]))

# requests.get('https://olimp.miet.ru/ppo_it/api').json()
data = get_all_tails('https://olimp.miet.ru/ppo_it/api')
map = [[] for _ in range(16)]
# print(*data, sep='\n')
# print('ok')


# print(dat1[::, 1].reshape(1, -1))
for el in data.copy():
    res = is_angels(el)
    if res != -1:
        map[res - 1] = np.array(el)
        data.remove(el)
for el in data.copy():
    res = f23(map[0], map[12], map[3], map[15], el)
    if res:
        map[res - 1] = el
    res2 = f59(map[0], map[12], map[3], map[15], el)
# print(*map, sep='\n')
print(map[0])
