---
title: Python Thread
tags: python
date: 2019-07-15
---

### GIL

GIL global interpreter lock (cpython)，python 中一个线程对应 C 语言的一个线程
GIL 使得同一时刻只有一个线程在一个 CPU 上执行，无法将多个线程映射到多个 CPU 上执行
GIL 会根据执行的字节码行数以及时间片释放 GIL ，在遇到 IO 操作时也会主动释放

运行

```python
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
```

```python
import threading

total = 0

def add():
    global total
    for _ in range(100000):
        total += 1


def dec():
    global total
    for _ in range(100000):
        total += 1



thread_add = threading.Thread(target=add)
thread_dec = threading.Thread(target=dec)

thread_add.start()
thread_dec.start()

thread_add.join()
thread_dec.join()

# GIL 会根据执行的字节码行数以及时间片释放 GIL, 所以 GIL 并不会保证绝对的线程安全
# total += 1, total -= 1 这种非原子操作对应字节码不是一步完成的
print(total) # 557
```

### 多线程的实现方式

- 通过 threading.Thread 实例化

- 继承 threading.Thread 实现 run 方法

threading.Thread 实例化

```python
import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html ended")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url ended")


thread1 = threading.Thread(target=get_detail_html, args=('',))
thread2 = threading.Thread(target=get_detail_url, args=('',))
# thread1.setDaemon(True) # 设置为后台线程，主线程执行完后自动销毁
# thread2.setDaemon(True)
start = time.time()
thread1.start()
thread2.start()
thread1.join()  # 等待 threa1 thread2 执行完毕，主线程才继续执行
thread2.join()
end = time.time()
print(f'cost time: { end - start }')
```

继承 threading.Thread 实现 run 方法

```python
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html ended")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url ended")


thread1 = GetDetailHtml('get_detail_html')
thread2 = GetDetailUrl('get_deatil_url')
start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()
print(f'cost time: { end - start }')
```

### 线程同步

使用锁可以防止多个线程对同一个变量的修改造成的不一致，锁的缺点是会影响性能并且容易引起死锁
RLock：可重入锁，在同一个线程可以连续调用锁的 acquire 和 release.

```python
import threading
from threading import Lock, RLock

total = 0
# lock = Lock()
lock = RLock()

def foo(lock):
    # 可重入
    lock.acquire()
    # dosomething
    lock.release()

def add(lock):
    global total
    # global lock
    for _ in range(1000000):
        lock.acquire()
        foo(lock)
        total += 1
        lock.release()


def dec(lock):
    global total
    # global lock
    for _ in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()



thread_add = threading.Thread(target=add, args=(lock,))
thread_dec = threading.Thread(target=dec, args=(lock,))

thread_add.start()
thread_dec.start()

thread_add.join()
thread_dec.join()

print(total) # 0
```

### 线程间通信

queue 包中的 Queue 可以实现线程间通信，并且 Queue 是线程安全的。

```python
import time
import threading
from queue import Queue


detail_url_queue = Queue(maxsize=1000)

def get_detail_html(queue):
    '''
    爬去文章详情页
    '''
    while True:
        # Queue 是线程安全的
        url = detail_url_queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html ended")


def get_detail_url(queue):
    '''
    爬去文章列表页
    '''
    # global detail_url_list
    while True:
        print("get detail url started")
        time.sleep(4)
        for i in range(20):
            queue.put(f'https://www.test.com/{i}')
        print("get detail url ended")



thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
for _ in range(10):
    thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
    thread_detail_html.start()
```

Thread_Local 全局变量 local_school 就是一个 ThreadLocal 对象，每个 Thread 对它都可以读写 student 属性，但互不影响。你可以把 local_school 看成全局变量，但每个属性如 local_school.student 都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal 内部会处理。

```python
import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('hello,%s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('python',),name='thread-a')
t2 = threading.Thread(target=process_thread,args=('ruby',),name='thread-b')
t1.start()
t2.start()
t1.join()
t2.join()
```

### 控制线程数量的锁 Semaphore

```python
import threading
import time
from threading import Semaphore


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('get {} data'.format(self.url))
        # 每次请求完 release, sem value + 1
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()  # 每次 value - 1,等于 0 的时候锁住, release 再加回来
            html_spider = HtmlSpider('http://www.test.com/{}'.format(i), self.sem)
            html_spider.start()

if __name__ == '__main__':
    # 控制进入数量为 3
    sem = Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
```

### 条件控制的锁 Condition

```python
import threading
from threading import Lock

# class StudentA(threading.Thread):
#     def __init__(self, name, lock):
#         super().__init__(name=name)
#         self.lock = lock

#     def run(self):
#         self.lock.acquire()
#         print(f'{self.name}: Hello BBB')
#         self.lock.release()

#         self.lock.acquire()
#         print(f'{self.name}: Where are you?')
#         self.lock.release()

# class StudentB(threading.Thread):
#     def __init__(self, name, lock):
#         super().__init__(name=name)
#         self.lock = lock

#     def run(self):
#         self.lock.acquire()
#         print(f'{self.name}: Hello AAA')
#         self.lock.release()

#         self.lock.acquire()
#         print(f'{self.name}: I am in Shanghai.')
#         self.lock.release()


from threading import Condition


class StudentA(threading.Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        # with:  self.cond.acquire()  self.cond.release()
        # 1. A cond lock, B 无法进入
        with self.cond:
            print(f'{self.name}: Hello BBB')
            # 2. A notify -> B wait
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: Where are you?')
            self.cond.notify()
            self.cond.wait()


class StudentB(threading.Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        with self.cond:
            # 3. B wait 获取另一个锁，可进入
            # 4. 释放 cond 锁
            self.cond.wait()
            print(f'{self.name}: Hello AAA')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: I am in Shanghai.')
            self.cond.notify()


if __name__ == '__main__':
    cond = Condition()
    sb = StudentB('BBB', cond)
    sa = StudentA('AAA', cond)
    # 调用顺序很重要
    # wait
    sb.start()
    sa.start()

# AAA: Hello BBB
# BBB: Hello AAA
# AAA: Where are you?
# BBB: I am in Shanghai.
```

### 线程池 ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED, ALL_COMPLETED
import time


def get_html(times):
    time.sleep(times)
    print('get {}'.format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
# print(task1.done(), task1.result())
# time.sleep(3)
# print(task1.done(), task1.result())

# urls = [3, 2, 4]
# all_tasks = [executor.submit(get_html, (url)) for url in urls]
# for future in as_completed(all_tasks):
#     data = future.result()
#     print('get {} success'.format(data))
# get 2
# get 2 success
# get 3
# get 3 success
# get 4
# get 4 succes


# urls = [3, 2, 4]
# for data in executor.map(get_html, urls):
#     print('get {} success'.format(data)
# 按照 urls 的顺序输出
# get 2
# get 3
# get 3 success
# get 2 success
# get 4
# get 4 success


urls = [3, 2, 4]
all_tasks = [executor.submit(get_html, (url)) for url in urls]
# 等待直到第一个完成
# wait(all_tasks, return_when=FIRST_COMPLETED)
wait(all_tasks, return_when=ALL_COMPLETED)
print('main')
```
