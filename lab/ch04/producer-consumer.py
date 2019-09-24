from threading import Thread
from collections import deque

import random
import time

MAX_DELAY = 3
MAX_LENGTH = 5
l = deque([])

def run_in_thread(func, args=[]):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def produce():
    global l
    cnt = 0
    while True:
        cnt += 1
        l.append(cnt)
        time.sleep(random.randint(1, MAX_DELAY))


def consume():
    global l
    while True:
        l.popleft()
        time.sleep(random.randint(1, MAX_DELAY))

if __name__=="__main__":
    run_in_thread(produce)
    run_in_thread(consume)
    time.sleep(60)