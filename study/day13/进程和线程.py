from random import randint
from time import time, sleep

from multiprocessing import Process, Queue
from os import getpid

from threading import Thread, Lock

# import time
import tkinter
import tkinter.messagebox

# def download_task(filname):
#     print(f'开始下载{filname}')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filname}下载完成，共用时{time_to_download}秒')
#
# def main():
#     start = time()
#     download_task('python从入门到入狱')
#     download_task('Peking Hot.avi')
#     end = time()
#     print(f'总耗时{end - start}秒')

"""
通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，它代表了传递给函数的参数。
"""
# def download_task1(filname):
#     print(f'启动下载进程，进程号{getpid()}')
#     print(f'开始下载{filname}...')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filname}下载完成，共用时{time_to_download}秒')
#
# def main():
#     start = time()
#     p1 = Process(target=download_task1, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task1, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print(f'文件下载完成，共用时{end - start}秒')

"""
多线程  使用threading模块的Thread类来创建线程
"""
# def download(filename):
#     print(f'开始下载{filename}...')
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f'{filename}下载完成，共耗时{time_to_download}秒')
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('python入门',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print(f'共耗时{end - start}秒')


"""
可以从已有的类创建新类，因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
"""
# class DownloadTask(Thread):
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename
#
#     def run(self):
#         print(f'开始下载{self._filename}...')
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print(f'{self._filename}下载完成，耗时{time_to_download}秒')
#
# def main():
#     start = time()
#     t1 = DownloadTask('python入门')
#     t1.start()
#     t2 = DownloadTask('Peking')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print(f'共耗时{end - start}秒')

"""
多个线程可以共享进程的内存空间
"""
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#
#     def deposit(self, money):
#         new_balance = self._balance + money
#         sleep(0.01)
#         self._balance = new_balance
#
#     @property
#     def balance(self):
#         return self._balance
#
# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._accunt = account
#         self._money = money
#
#     def run(self):
#         self._accunt.deposit(self._money)
#
# def main():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print(f'账户余额为： ￥{account.balance}元')

"""
使用“锁”保护数据
"""
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print(f'账户余额为： ￥{account.balance}元')


"""
单线程+异步I/O
"""
# def download():
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成')
#
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者：张三')
#
#
# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()

"""
使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程
"""
# def main():
#     class DownloadTaskHandler(Thread):
#
#         def run(self):
#             sleep(10)
#             tkinter.messagebox.showinfo('提示','下载完成')
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         button1.config(state=tkinter.DISABLED)
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于', '作者：张三')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()

"""
使用多进程对复杂任务进行“分而治之”。
"""
# def main():
#     total = 0
#     number_list = [x for x in range(1, 10000001)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print(f'Execution time: {end - start}s')


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        num = int(10000000/8)
        p = Process(target=task_handler, args=(number_list[index:index + num], result_queue))
        index += num
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print(f'Execution time: {end - start}s')


if __name__ == '__main__':
    main()
