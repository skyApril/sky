# from time import time, localtime, sleep
# class Clock(object):
#     """数字时钟"""
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         print(ctime)
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
# def main():
#     # 通过类方法创建对象并获取系统时间
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     main()

# class Person(object):
#     """人"""
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     @property
#     def name(self):
#         return self._name
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def play(self):
#         print('%s正在愉快的玩耍.' % self._name)
#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片.' % self._name)
#         else:
#             print('%s只能观看《熊出没》.' % self._name)
#
# class Student(Person):
#     """学生"""
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#     @property
#     def grade(self):
#         return self._grade
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))
#
# class Teacher(Person):
#     """老师"""
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#     @property
#     def title(self):
#         return self._title
#     @title.setter
#     def title(self, title):
#         self._title = title
#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))
#
# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('骆昊', 38, '砖家')
#     t.teach('Python程序设计')
#     t.watch_av()
#
#
# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractmethod
# class Pet(object, metaclass=ABCMeta):
#     """宠物"""
#     def __init__(self, nickname):
#         self._nickname = nickname
#     @abstractmethod
#     def make_voice(self):
#         """发出声音"""
#         pass
#
# class Dog(Pet):
#     """狗"""
#     def make_voice(self):
#         print('%s: 汪汪汪...' % self._nickname)
#
# class Cat(Pet):
#     """猫"""
#     def make_voice(self):
#         print('%s: 喵...喵...' % self._nickname)
#
# def main():
#     pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
#     for pet in pets:
#         pet.make_voice()
#
# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
#
# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#     # 通过__slots__魔法限定对象可以绑定的成员变量
#     __slots__ = ('_name', '_hp')
#     def __init__(self, name, hp):
#         """初始化方法
#         :param name: 名字
#         :param hp: 生命值
#         """
#         self._name = name
#         self._hp = hp
#     @property
#     def name(self):
#         return self._name
#     @property
#     def hp(self):
#         return self._hp
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
#     @property
#     def alive(self):
#         return self._hp > 0
#     @abstractmethod
#     def attack(self, other):
#         """攻击
#         :param other: 被攻击的对象
#         """
#         pass
#
# class Ultraman(Fighter):
#     """奥特曼"""
#     __slots__ = ('_name', '_hp', '_mp')
#     def __init__(self, name, hp, mp):
#         """初始化方法
#         :param name: 名字
#         :param hp: 生命值
#         :param mp: 魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#     def huge_attack(self, other):
#         """究极必杀技(打掉对方至少50点或四分之三的血)
#         :param other: 被攻击的对象
#         :return: 使用成功返回True否则返回False
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
#     def magic_attack(self, others):
#         """魔法攻击
#         :param others: 被攻击的群体
#         :return: 使用魔法成功返回True否则返回False
#         """
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
#     def resume(self):
#         """恢复魔法值"""
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp + \
#             '魔法值: %d\n' % self._mp
#
# class Monster(Fighter):
#     """小怪兽"""
#     __slots__ = ('_name', '_hp')
#     def attack(self, other):
#         other.hp -= randint(10, 20)
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp
#
# def is_any_alive(monsters):
#     """判断有没有小怪兽是活着的"""
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
# def select_alive_one(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')
#
# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('狄仁杰', 250)
#     m2 = Monster('白元芳', 500)
#     m3 = Monster('王大锤', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#         print('========第%02d回合========' % fight_round)
#         m = select_alive_one(ms)  # 选中一只小怪兽
#         skill = randint(1, 10)   # 通过随机数选择使用哪种技能
#         if skill <= 6:  # 60%的概率使用普通攻击
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用魔法失败.' % u.name)
#         else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
#         fight_round += 1
#     print('\n========战斗结束!========\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利!' % u.name)
#     else:
#         print('小怪兽胜利!')
#
# if __name__ == '__main__':
#     main()

# import json
#
#
# def main():
#     mydict = {
#         'name': '骆昊',
#         'age': 38,
#         'qq': 957658,
#         'friends': ['王大锤', '白元芳'],
#         'cars': [
#             {'brand': 'BYD', 'max_speed': 180},
#             {'brand': 'Audi', 'max_speed': 280},
#             {'brand': 'Benz', 'max_speed': 320}
#         ]
#     }
#     try:
#         with open('data.json', 'w', encoding='utf-8') as fs:
#             json.dump(mydict, fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成!')
#
#
# if __name__ == '__main__':
#     main()

# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep
#
#
# def download_task(filename):
#     print('启动下载进程，进程号[%d].' % getpid())
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()

# from random import randint
# from threading import Thread
# from time import time, sleep
#
#
# def download(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))
#
#
# def main():
#     start = time()
#     t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
#     t1.start()
#     t2 = Thread(target=download, args=('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒' % (end - start))
#
#
# if __name__ == '__main__':
#     main()

# from time import sleep
# from threading import Thread
# class Account(object):
#     def __init__(self):
#         self._balance = 0
#     def deposit(self, money):
#         # 计算存款后的余额
#         new_balance = self._balance + money
#         # 模拟受理存款业务需要0.01秒的时间
#         sleep(0.01)
#         # 修改账户余额
#         self._balance = new_balance
#     @property
#     def balance(self):
#         return self._balance
#
# class AddMoneyThread(Thread):
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#     def run(self):
#         self._account.deposit(self._money)
#
# def main():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
#     main()

# from time import sleep
# from threading import Thread, Lock
#
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         # 先获取锁才能执行后续的代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             # 在finally中执行释放锁的操作保证正常异常锁都能释放
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
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
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
#     main()

import time
import tkinter
# import tkinter.messagebox
# def download():
#     # 模拟下载任务需要花费10秒钟时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示', '下载完成!')
#
# def show_about():
#     tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
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
#
# if __name__ == '__main__':
#     main()

# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
# def main():
#     class DownloadTaskHandler(Thread):
#         def run(self):
#             time.sleep(10)
#             tkinter.messagebox.showinfo('提示', '下载完成!')
#             # 启用下载按钮
#             button1.config(state=tkinter.NORMAL)
#
#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
#         # 在线程中处理耗时间的下载任务
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost', 1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=show_about)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# from time import time
# def main():
#     total = 0
#     number_list = [x for x in range(1, 100000001)]
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Execution time: %.3fs' % (end - start))
#
# if __name__ == '__main__':
#     main()

# from multiprocessing import Process, Queue
# from random import randint
# from time import time
#
#
# def task_handler(curr_list, result_queue):
#     total = 0
#     for number in curr_list:
#         total += number
#     result_queue.put(total)
#
#
# def main():
#     processes = []
#     number_list = [x for x in range(1, 100000001)]
#     result_queue = Queue()
#     index = 0
#     # 启动8个进程将数据切片后进行运算
#     for _ in range(8):
#         p = Process(target=task_handler,
#                     args=(number_list[index:index + 12500000], result_queue))
#         index += 12500000
#         processes.append(p)
#         p.start()
#     # 开始记录所有进程执行完成花费的时间
#     start = time()
#     for p in processes:
#         p.join()
#     # 合并执行结果
#     total = 0
#     while not result_queue.empty():
#         total += result_queue.get()
#     print(total)
#     end = time()
#     print('Execution time: ', (end - start), 's', sep='')
#
#
# if __name__ == '__main__':
#     main()

# from time import time
# from threading import Thread
# import requests
# # 继承Thread类创建自定义的线程类
# class DownloadHanlder(Thread):
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#     def run(self):
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('/Users/Hao/' + filename, 'wb') as f:
#             f.write(resp.content)
# def main():
#     # 通过requests模块的get函数获取网络资源
#     # 下面的代码中使用了天行数据接口提供的网络API
#     # 要使用该数据接口需要在天行数据的网站上注册
#     # 然后用自己的Key替换掉下面代码的中APIKey即可
#     resp = requests.get(
#         'http://api.tianapi.com/meinv/?key=APIKey&num=10')
#     # 将服务器返回的JSON格式的数据解析为字典
#     data_model = resp.json()
#     print(data_model)
#     # for mm_dict in data_model['newslist']:
#     #     url = mm_dict['picUrl']
#     #     # 通过多线程的方式实现图片下载
#     #     DownloadHanlder(url).start()
#
# if __name__ == '__main__':
#     main()

# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
# def main():
#     # 1.创建套接字对象并指定使用哪种传输服务
#     # family=AF_INET - IPv4地址
#     # family=AF_INET6 - IPv6地址
#     # type=SOCK_STREAM - TCP套接字
#     # type=SOCK_DGRAM - UDP套接字
#     # type=SOCK_RAW - 原始套接字
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 2.绑定IP地址和端口(端口用于区分不同的服务)
#     # 同一时间在同一个端口上只能绑定一个服务否则报错
#     server.bind(('192.168.101.21', 6789))
#     # 3.开启监听 - 监听客户端连接到服务器
#     # 参数512可以理解为连接队列的大小
#     server.listen(512)
#     print('服务器启动开始监听...')
#     while True:
#         # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
#         # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         # accept方法返回一个元组其中的第一个元素是客户端对象
#         # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器.')
#         # 5.发送数据
#         client.send(str(datetime.now()).encode('utf-8'))
#         # 6.断开连接
#         client.close()
#
#
# if __name__ == '__main__':
#     main()

# import datetime
#
# from openpyxl import Workbook
#
# wb = Workbook()
# ws = wb.active
#
# ws['A1'] = 42
# ws.append([1, 2, 3])
# ws['A2'] = datetime.datetime.now()
#
# wb.save("sample.xlsx")

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)