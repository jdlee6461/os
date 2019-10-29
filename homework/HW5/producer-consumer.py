from threading import Thread
from collections import deque

import random
import time

MAX_DELAY = 3
MAX_LENGTH = 5
l = []
cnt = 0

def run_in_thread(func, args=[]):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def produce():
    global l
    global cnt
    while True:
        while len(l) >= MAX_LENGTH:
            continue

        cnt += 1
        l.append(cnt)

        print("Produced! Current list: %s" % (str(l)))            


def consume():
    global l
    global cnt
    while True:
        while len(l) <= 0:
            continue

        cnt -= 1
        l.pop()

        print("Consumed! Current list: %s" % (str(l)))            

if __name__=="__main__":
    run_in_thread(produce, [])
    run_in_thread(consume, [])
    time.sleep(60)