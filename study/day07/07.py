"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""
# m = int(input('m= '))
# n = int(input('n= '))
# fm = 1
# for num in range(1, m+1):
#     fm *= num
# fn = 1
# for num in range(1, n+1):
#     fn *= num
# fm_n = 1
# for num in range(1, m-n+1):
#     fm_n *= num
# print(fm // fn // fm_n)
#
# fa = 1
# for num in range(m,m-n,-1):
#     fa *= num
# fb = 1
# for num in range(1,n+1):
#     fb *= num
# print(fa,fb, fa/fb)
# def fac(num):
#     result = 1
#     for n in range(1, num+1):
#         result *= n
#     return result
# m = int(input('m = '))
# n = int(input('n = '))
# print(fac(m) // fac(n) // fac(m-n))


# from random import randint
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1,6)
#     return total
#
# def add(a=0,b=0,c=0):
#     return a + b + c
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
# # 在调用add函数时可以传入0个或多个参数
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))


# def foo():
#     print('hello, world!')
#
#
# def foo():
#     print('goodbye, world!')
#
#
# # 下面的代码会输出什么呢？goodbye, world!
# foo()


























