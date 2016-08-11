#coding:utf-8
import threading
from Queue import Queue

myqueue = Queue(100)
for i in range(100):
    myqueue.put('task%d'%(i+1))

def foo():
    try:
        task = myqueue.get_nowait()
        with open('thread.txt','a') as f:
            f.write('%s finished!'%task+'\n')
    except Exception,e:
        pass
    #print '%s execute!'%task
    

class myThread(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func =func
    def run(self):
        while myqueue.qsize() > 0:
            self.func()
            print self.getName()

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
