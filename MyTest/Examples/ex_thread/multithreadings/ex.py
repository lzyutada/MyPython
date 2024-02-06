import _thread
import time

# 为线程定义一个函数
def __print_time1( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def func1() :
    '''
    using _thread, i.e thread of py2
    '''
    # 创建两个线程
    try:
        _thread.start_new_thread(__print_time1, ("Thread-1", 2, ) )
        _thread.start_new_thread(__print_time1, ("Thread-2", 4, ) )
    except:
        print ("Error: 无法启动线程")

    while 1:
        pass

def func2() :
    '''
    threading for py3
    '''
    import threading
    import time
    class myThread (threading.Thread):
        __exitFlag1 = 0
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
        def run(self):
            print ("开始线程：" + self.name)
            self.__print_time2(self.name, self.delay, 5)
            print ("退出线程：" + self.name)

        def __print_time2(self, threadName, delay, counter):
            while counter:
                if myThread.__exitFlag1:
                    threadName.exit()
                time.sleep(delay)
                print ("%s: %s" % (threadName, time.ctime(time.time())))
                counter -= 1

    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 1.5)
    # 开启新线程
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print ("退出主线程")

def func3() :
    '''threads sync without lock'''#!/usr/bin/python3

    class Dto :
        def __init__(that, n, v) :
            that.name = n
            that.value = v
    datalist = [
        Dto('n1', 0),
        Dto('n2', 0),
        Dto('n3', 0),
        Dto('n4', 0),
        Dto('n5', 0),
        ]

    import threading
    import time
    class myThread1 (threading.Thread):
        '''set to 0'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = len(datalist) - 1
        def run(self):
            print ("开启线程： " + self.name)
            # threadLock.acquire()    # 获取锁，用于线程同步
            while -1 < self.index :
                time.sleep(self.delay)
                print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                datalist[self.index].value = 1
                self.index = self.index - 1
            # threadLock.release()    # 释放锁，开启下一个线程

    class myThread2 (threading.Thread):
        '''print element'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = 0
        def run(self):
            print ("开启线程： " + self.name)
            # threadLock.acquire()    # 获取锁，用于线程同步
            while len(datalist) > self.index :
                time.sleep(self.delay)
                print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                self.index = self.index + 1
            # threadLock.release()    # 释放锁，开启下一个线程

    # 创建新线程
    t1 = myThread1(1, "Thread-1", 0.5)
    t2 = myThread2(2, "Thread-2", 0.1)

    # 开启新线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print ("退出主线程")

def func4() :
    '''threads sync with lock'''#!/usr/bin/python3

    class Dto :
        def __init__(that, n, v) :
            that.name = n
            that.value = v
    datalist = [
        Dto('n1', 0),
        Dto('n2', 0),
        Dto('n3', 0),
        Dto('n4', 0),
        Dto('n5', 0),
        ]

    import threading
    import time
    class myThread1 (threading.Thread):
        '''set to 0'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = len(datalist) - 1
        def run(self):
            print ("开启线程： " + self.name)
            threadLock.acquire()    # 获取锁，用于线程同步
            while -1 < self.index :
                time.sleep(self.delay)
                print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                datalist[self.index].value = 1
                self.index = self.index - 1
            threadLock.release()    # 释放锁，开启下一个线程

    class myThread2 (threading.Thread):
        '''print element'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = 0
        def run(self):
            print ("开启线程： " + self.name)
            threadLock.acquire()    # 获取锁，用于线程同步
            while len(datalist) > self.index :
                time.sleep(self.delay)
                print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                self.index = self.index + 1
            threadLock.release()    # 释放锁，开启下一个线程

    threadLock = threading.Lock()
 
    # 创建新线程
    t1 = myThread1(1, "Thread-1", 0.5)
    t2 = myThread2(2, "Thread-2", 0.1)

    # 开启新线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print ("退出主线程")

def func5() :
    '''threads sync with lock, using with @lockname'''#!/usr/bin/python3

    class Dto :
        def __init__(that, n, v) :
            that.name = n
            that.value = v
    datalist = [
        Dto('n1', 0),
        Dto('n2', 0),
        Dto('n3', 0),
        Dto('n4', 0),
        Dto('n5', 0),
        ]

    import threading
    import time
    class myThread1 (threading.Thread):
        '''set to 0'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = len(datalist) - 1
        def run(self):
            print ("开启线程： " + self.name)
            with threadLock: 
                while -1 < self.index :
                    time.sleep(self.delay)
                    print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                    datalist[self.index].value = 1
                    self.index = self.index - 1

    class myThread2 (threading.Thread):
        '''print element'''
        def __init__(self, threadID, name, delay):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.delay = delay
            self.index = 0
        def run(self):
            print ("开启线程： " + self.name)
            with threadLock: 
                while len(datalist) > self.index :
                    time.sleep(self.delay)
                    print ("%s: %s, %s, %s" % (self.name, datalist[self.index].name, datalist[self.index].value, time.ctime(time.time())))
                    self.index = self.index + 1

    threadLock = threading.Lock()
 
    # 创建新线程
    t1 = myThread1(1, "Thread-1", 0.5)
    t2 = myThread2(2, "Thread-2", 0.1)

    # 开启新线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print ("退出主线程")

def func6() :
    '''
    about queue
    '''
    import queue
    import threading
    import time

    exitFlag = 0

    class myThread (threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q
        def run(self):
            print ("开启线程：" + self.name)
            self.__process_data()
            print ("退出线程：" + self.name)

        def __process_data(that):
            while not exitFlag:
                with queueLock: 
                    if not workQueue.empty():   # 'workQueue' is queue, same as 'q'
                        data =that.q.get()          # 'q' is queue, same as 'workQueue'
                        print ("%s processing %s" % (that.name, data))
                time.sleep(1)

    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)
    threads = []; threadID = 1

    # 创建新线程
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start(); print("%s was started, size of workQueue is %d" % (tName, workQueue.qsize()))
        threads.append(thread); print("%s was appended to threads" % (tName))
        threadID += 1

    with queueLock: # 填充队列
        print("main thread acquired the mutex")
        for word in nameList: 
            workQueue.put(word)
            print("%s added to workQueue, size is %d" % (word, workQueue.qsize()))
        print("main thread release the mutex")

    while not workQueue.empty(): pass # 等待队列清空
    print("workQueue is empty, ", workQueue.qsize())
    exitFlag = 1 # 通知线程是时候退出
    
    for t in threads: t.join() # 等待所有线程完成

    print ("退出主线程")
