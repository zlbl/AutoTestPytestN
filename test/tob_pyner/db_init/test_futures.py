# -*- coding:utf-8 -*-
from concurrent import futures


def test(num):
    import time
    time.sleep(1)
    return time.ctime(), num


def test_something():
    data = [1, 2, 3]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        for future in executor.map(test, data):
            print(future)
