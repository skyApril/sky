"""
水仙花  水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""
# for i in range(100, 1000):
#     low = i % 10
#     mid = i // 10 % 10
#     high = i // 100
#     if i == low ** 3 + mid ** 3 + high ** 3:
#         print(i)

"""
正数反转
"""
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)

"""
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))

"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""
# from random import randint
#
# money = 1000
# while money > 0:
#     print('你的资产为：', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注： '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了，游戏结束！')

"""
生成斐波那契数列的前20个数  斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""
# nums = [1, 1]
# for i in range(0,18):
#     nums.append(nums[i]+nums[i+1])
# print(nums, len(nums))

"""
找出10000以内的完美数  它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
"""
# perfectNum = []
# for i in range(1, 10000):
#     num = []
#     for j in range(1, i):
#         if i % j == 0:
#            num.append(j)
#     # print(num)
#     if i == sum(num):
#         perfectNum.append(i)
# print(perfectNum)

"""
输出100以内所有的素数  素数指的是只能被1和自身整除的正整数（不包括1）
"""
# num = []
# for i in range(2,100):
#     for j in range(1, i-1):
#         if i % j != 0:
#             num.append(i)
# print(num)

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')