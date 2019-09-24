from threading import Thread
import time
import threading

def run_in_thread(func, args=[]):
    t = Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()

def count(cnt, p):
    global value
    for i in range(cnt):
        print("%d: %d" % (threading.get_ident(), i+1))
        time.sleep(p)

if __name__=="__main__":
    count(5, 1)
    count(5, 2)
"""
    run_in_thread(count, [5, 1])
    run_in_thread(count, [5, 2])
    time.sleep(10)
"""
