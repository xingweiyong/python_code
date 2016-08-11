#coding:utf-8
import threading
from Queue import Queue

myqueue = Queue(1000)
for i in range(1000):
    myqueue.put('task%d'%(i+1))

def foo():
    try:
        task = myqueue.get_nowait()
    except Exception,e:
        pass
    #print '%s execute!'%task
    with open('thread.txt','a') as f:
        f.write('%s finished!'%task+'\n')

class myThread(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func =func
    def run(self):
        while myqueue.qsize() > 0:
            self.func()

def main():
    threads = []
    for i in range(30):
        t = myThread(foo)
        threads.append(t)

    for i in range(30):
        threads[i].start()

    for i in range(30):
        threads[i].join()


main()
