# prices = {
#     'AAPL': 191.88,
#     'GOOG': 432.848,
#     'UIBM': 1921.838,
#     'OTV': 19.13,
#     'WSDD': 43.22,
#     'WDQ': 3332.8218,
# }
#
# prices2 = { key: value for key, value in prices.items() if value > 100 }
# print(prices2)


# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
#
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
#         print(scores)



# import  heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
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
# itertools.permutations('ABCD')
# # 产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))



# 普通排序
def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) -1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

print(select_sort([1,2,3,4,6,2,12,3,42,232]))


# 冒泡排序
def bubble_sort(items, comp=lambda x, y: x> y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

print(bubble_sort([534,2,3,4,6,1,12,3,42,232]))










