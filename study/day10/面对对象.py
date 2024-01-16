# 使用class关键字定义类
# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))
#
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看电影.' % self.name)
#
# # 使用定义的类
# def main():
#     stu1 = Student('张三',18)
#     stu1.study('孙子兵法')
#     stu1.watch_movie()
#     stu2 = Student('李四',14)
#     stu2.study('刑法')
#     stu2.watch_movie()


# 访问可见性问题
# class Test:
#
#     def __init__(self, foo):
#         self._foo = foo
#
#     def _bar(self):
#         print(self._foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     test._bar()
#     print(test._foo)

# class Test:
#
#     def __init__(self, foo):
#         self.__foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)
#
#






# 定义一个类描述数字时钟。
# from time import sleep
#
# class Clock(object):
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % \
#             (self._hour, self._minute, self._second)
#
# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()



# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 访问器
#     @property
#     def name(self):
#         return self._name
#
#     # 访问器
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在完飞行棋' % self._name)
#         else:
#             print('%s正在玩斗地主' % self._name)
#
# def main():
#     person = Person('张三', 18)
#     person.play()
#     person.age = 12
#     person.play()



# __slots__魔法
# class Person(object):
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
#
#     @property
#     def name(self):
#         return  self._name
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
#             print('%s正在玩耍' % self._name)
#         else:
#             print('%s正在工作,%s' % (self._name, self._gender))
# def main():
#     person = Person('王大锤', 22, '女')
#     person._gender = '男'
#     person.play()



# 静态方法和类方法
# from math import sqrt
#
# # 传入的三条边长是否能构造出三角形对象
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod #静态方法
#     def is_valid(a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
#
# def main():
#     a, b, c = 3, 4, 5
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         print(t.area())
#     else:
#         print('无法构成三角形')


# from time import time, localtime, sleep
# class Clock(object):
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
#
# def main():
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()



# 继承和多态
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return (self._name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print(f"{self._name}正在愉快的玩耍")

    def watch_av(self):
        if self._age >= 18:
            print(f"{self._name}正在观看电影")
        else:
            print(f"{self._name}正在看熊出没")


class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f"{self._grade}的{self._name}正在学习{course}")


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f"{self._name}{self._title}正在学习{course}")


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()

if __name__ == "__main__":
    main()






