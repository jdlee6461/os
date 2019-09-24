from threading import Thread
import time
import threading

value = 5

def run_in_thread(func, args=[]):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def dummy():
    print(threading.get_ident())
    while True:
        continue

def count(cnt, p):
    global value
    for i in range(cnt):
        #print("%d: %d" % (threading.get_ident(), i+1))
        value += 1
        print(value)
        time.sleep(p)

if __name__=="__main__":
    for i in range(60000):
       run_in_thread(dummy, [])

"""
    run_in_thread(count, [5, 1])
    run_in_thread(count, [5, 2])
    time.sleep(10)
"""
