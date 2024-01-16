"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""

# import heapq
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


"""
迭代工具模块
"""
# import itertools
#
# # 产生ABCD的全排列
# a = itertools.permutations('ABCD')
# # for p in a:
# #     print(p)
# # 产生ABCDE的五选三组合
# b= itertools.combinations('ABCDE', 3)
# for j in b:
#     print(j)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))

"""
找出序列中出现次数最多的元素
"""
# from collections import Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(5))

# a = 321
# b = 12
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# type 检查类型
# a = 100
# b = 12.345
# c = 1 + 5j
# d = "hello, woeld"
# e = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(int('100', 2)) # int() 将一个数值或字符串转换为整数，可以指定进制
# print(float('123123')) # float() 将一个字符串转换成浮点数
# print(str({'aa': '11'}))  # str() 将指定的对象转换成字符串形式，可以指定编码
# print(chr(65)) # 用于将 Unicode 码点转换为对应的字符
# print(ord('\x08')) #用于返回一个字符的 Unicode 码点（code point）

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %d' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
# not 取反   or 一个为真就为真   and 一个为假就为假


# a = 10
# b = 3
# a += b  # a = a + b
# a *= a + 2 # a = a * (a + 2)
# print(a)

# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not(1 != 2)
# print('flag0 =', flag0)
# print('flag1 =', flag1)
# print('flag2 =', flag2)
# print('flag3 =', flag3)
# print('flag4 =', flag4)
# print('flag5 =', flag5)

# f = float(input('请输入华氏温度：'))
# c = (f - 32)/1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
输入圆的半径计算圆的周长和面积 
"""
# r = float(input('情输入半径：'))
# perimeter = 2 * r * 3.1416
# area = 3.1416 * r * r
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

"""
输入年份判断是不是闰年。
"""
# year = int(input('请输入年份：'))
# is_leap = year % 4 == 0 and year % 100 != 0 or \
#           year % 400 == 0
# print(is_leap)

"""
用for循环实现1~100求和
"""
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)  # 5050

"""
用for循环实现1~100之间的偶数求和
"""
# sum = 0
# for i in range(2, 101, 2):
#     sum += i
# print(sum) # 2550
#
# num = 0
# for x in range(101):
#     if x % 2 == 0:
#         num += x
# print(num)

"""
猜数字游戏
break 终止它所在的那个循环
continue 放弃本次循环后续的代码直接让循环进入下一轮
"""
# import  random
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的猜的次数太多了')

"""
九九乘法口诀
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d * %d = %d' % (j, i, i*j), end='\t')
#     print()
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

"""
输入一个正整数判断是不是素数
"""
# a = int(input('请输入正整数：'))
# num = 0
# for x in range(1, a+1):
#     if a % x == 0:
#        num +=1
# if num > 2:
#     print('不是素数')
# else:
#     print('是素数')
# print(num)

# from math import sqrt
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# print(end)
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

"""
输入两个正整数，计算它们的最大公约数和最小公倍数。
"""
# x = int(input('x= '))
# y = int(input('y= '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor)) # // 整除运算符
#         break

"""
打印三角形图案
"""
row = int(input('请输入行数： '))
# for i in range(row):
#     for _ in range(i+1):
#         print('*', end='')
#     print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

for i in range(row):
    print(i)
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()





































