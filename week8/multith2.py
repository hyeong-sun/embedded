import threading
import os
import time

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    a=1
    while True:
        print('thread 1')
        time.sleep(1.0)
        a=a+1
        if a>5: break
    
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    a=1
    while True:
        print('thread 2')
        time.sleep(1.0)
        a=a+1
        if a>5: break    


if __name__=="__main__":
    print("ID of process main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.main_thread().name))
    
    t1 = threading.Thread(target=task1,args='t1')
    t2 = threading.Thread(target=task2,args='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")