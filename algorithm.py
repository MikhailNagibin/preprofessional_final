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

def is_neighbors(data, data1):
    pass