import time
from time import sleep
from threading import Thread, Event, Lock

# """
# 线程 创建示例
# """
#
# import threading
# from time import sleep
# import os
#
# a = 1  # 全局变量
#
#
# # 线程执行函数
# def music():
#     global a
#     print("a = ", a)
#     a = 10000
#     for i in range(3):
#         sleep(2)
#         print(os.getpid(), "播放： 葫芦娃")
#
#
# # 创建线程
# t = threading.Thread(target=music)
# # 启动线程
# t.start()
#
# # 主线程继续执行
# for i in range(4):
#     sleep(1)
#     print(os.getpid(), "播放：eight")
#
# # 等待回收线程
# t.join()
# print("a:", a)  # 10000


"""多线程"""

# def func(sec, name):
#     print("含有参数的线程函数")
#     sleep(sec)
#     print(f"{name}线程执行完毕")
#
#
# jobs = []
# for i in range(5):
#     t = Thread(target=func, args=(2, f"达内-{i}"))
#     jobs.append(t)
#     t.start()
#
# for job in jobs:
#     job.join()

"""自定义线程类"""

# class MyThread(Thread):
#     def __init__(self, song):
#         self.song = song
#         super(MyThread, self).__init__()
#
#     def run(self):
#         for i in range(3):
#             print(f"播放:{self.song}")
#             sleep(2)
#
#
# t = MyThread("凉凉")
# t.start()
# t.join()


"""练习:售票系统模拟"""
# t_list = [f"T{i}" for i in range(1, 501)]
#
#
# def sell_ticket(window):
#     # while True:
#     #     if t_list:
#     #         print(f"{window}----{t_list[0]}")
#     #         del t_list[0]
#     #         sleep(0.1)
#     #         continue
#     #     print(f"{window}所有票已售完")
#     #     break
#     while t_list:
#         print(f"{window}----{t_list.pop(0)}")
#         sleep(0.1)
#     else:
#         print(f"{window}所有票已售完")
#
#
# jobs = []
# for i in range(1, 11):
#     window = f"w{i}"
#     t = Thread(target=sell_ticket, args=(window,))
#     jobs.append(t)
#     t.start()
#
# for job in jobs:
#     job.join()


"""线程同步互斥方法"""

"""
    线程Event
"""
# msg = None  # 用于线程通信的全局变量
#
# e = Event()
#
#
# # 线程函数
# def 杨子荣():
#     print("杨子荣前来拜山头")
#     global msg
#     msg = "天王盖地虎"
#     e.set()
#
#
# t = Thread(target=杨子荣)
# t.start()
# e.wait()
# print("说对口令就是自己人")
# if msg == "天王盖地虎":
#     print("宝塔镇河妖")
#     print("是自己人")
# else:
#     print("打死他...无情啊...")
# t.join()

"""
    线程锁Lock
"""

# a = b = 0
# lock = Lock()
#
#
# def value():
#     while True:
#         lock.acquire()
#         if a != b:
#             print(f"a={a},b={b}")
#         lock.release()
#
#
# t = Thread(target=value)
# t.start()
#
# while True:
#     # lock.acquire()
#     # a += 1
#     # b += 1
#     # lock.release()
#     with lock:
#         a += 1
#         b += 1
# t.join()


"""练习:同步互斥"""
"""
此法不能打印字母

# letters = [chr(i) for i in range(65, 91)]
# nums = [i for i in range(1, 53, 2)]
# 
# 
# def out_letter():
#     while letters:
#         letters.pop(0)
# 
# 
# def out_num():
#     while nums:
#         print(nums[0], nums[0] + 1, sep="")
#         del nums[0]

"""


#
# lock1 = Lock()
# lock2 = Lock()
# lock2.acquire()
#
#
# def out_num():
#     for i in range(1, 53, 2):
#         lock1.acquire()
#         print(i, i + 1, sep="", end="")
#         lock2.release()
#
#
# t1 = Thread(target=out_num)
#
#
# def out_letter():
#     for i in range(65, 91):
#         lock2.acquire()
#         print(chr(i), sep="")
#         lock1.release()
#
#
# t2 = Thread(target=out_letter)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_sum(start, end):
    result = 0
    for i in range(start, end):
        if is_prime(i):
            result += i
    print(result, end=",")


def get_run_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        print(f"\b\n用时:{end - start}秒")

    return wrapper


@get_run_time
def main():
    jobs = []
    for i in range(1, 100001, 10000):
        t = Thread(target=get_sum, args=(i, i + 10000))
        jobs.append(t)
        t.start()
    for job in jobs:
        job.join()


if __name__ == '__main__':
    main()
    print(sum((32405717,
               88607591,
               141060794,
               192322435)))  # 454396537
