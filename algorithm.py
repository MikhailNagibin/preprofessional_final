import numpy as np


def is_angels(data):
    tail = np.array(data)
    if tail[0] == [255] * 64:
        if tail[::, 0] == [255] * 64:
            return 1
        return 4
    if tail[-1] == [255] * 64:
        if tail[::, 0] == [255] * 64:
          return 13
        return 16
    return -1

def is_neighbors(data, data1):
    pass