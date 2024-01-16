#Wait Async
#By Sparksammy
import thread
import time


def wait(time2wait):
    timeEnd = time2wait + time.time()
    timer = thread.allocate_lock()
    with timer:
        while True:
            if time.time() >= timeEnd:
                break

def waitAndExec(time2wait, execAfter):
    timer = thread.allocate_lock()
    currTime = 0
    timeEnd = time2wait + time.time()
    with timer:
        while True:
            if time.time() >= timeEnd:
                break
        exec(execAfter)