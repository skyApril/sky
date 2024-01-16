"""
生成式（推导式）的用法
"""
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
#
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)


# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)


"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
heapq.nlargest 最大的
heapq.nsmallest 最小的
"""
# import heapq
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
# print(heapq.nlargest(3, list2, key=lambda x: x['price']))
# print(heapq.nlargest(3, list2, key=lambda x: x['shares']))


"""
迭代工具模块
"""
# import itertools
# # 产生ABCD的全排列
# itertools.permutations('ABCD')
# # 产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))


# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
# items2 = [x ** 2 for x in range(1, 10) if x % 2]
# print(items1)
# print(items2)
# print(list(filter(lambda x: x % 2, range(1, 10))))


#
# from functools import wraps
# from time import time
#
# def record(output):
#     """可以参数化的装饰器"""
#
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args, **kwargs)
#             output(func.__name__, time() - start)
#             return result
#
#         return wrapper
#
#     return decorate





"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 150000.0

class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour

class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales *0.05

class EmployeeFactory:

    @staticmethod
    def create(emp_type, *args, **kwargs):
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()






























