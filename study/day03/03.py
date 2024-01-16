# class Person(object):
#
#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 22)
#     person.play()
#     person._gender = '男'
#
# if __name__ == '__main__':
#     main()

from math import sqrt
class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))
def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')
if __name__ == '__main__':
    main()
