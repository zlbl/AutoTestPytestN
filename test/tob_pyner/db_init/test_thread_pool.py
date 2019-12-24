from concurrent.futures import ThreadPoolExecutor
import time
import threading

pool = ThreadPoolExecutor(128)


def echo_client(abc):
    time.sleep(2)
    print("abc is %s time is %s" % (time.time(), abc,))


def test_echo_server():
    for i in range(10):
        # pool.submit(echo_client, str(i))
        time.sleep(3)
        t1 = threading.Thread(target=echo_client, args=(str(i),))
        t1.start()
