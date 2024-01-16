# s1 = 'hello, world!'
# s2 = "hello, world!"
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='')

"""
可以在字符串中使用（反斜杠）来表示转义，也就是说后面的字符不再是它原来的意义，
例如：\n不是代表反斜杠和字符n，而是表示换行；而\t也不是代表反斜杠和字符t，而是表示制表符。
所以如果想在字符串中表示'要写成\'，同理想表示要写成\\。
"""
import sys

# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# list1 = [1, 3, 5, 7, 100]
# for index in range(len(list1)):
#     print(list1[index])
# for elem in list1:
#     print(elem)
# for index, elem in enumerate(list1):
#     print(index, elem)
# list1.append(200)
# list1.insert(1,400)
# list1 += [1000, 2000]
# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
#
# list1.pop(0)
# list1.pop(len(list1) - 1)
# list1.clear()
# print(len(list1))
# print(list1)


# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# print(fruits)
# fruits2 = fruits[1:4]
# fruits3 = fruits[:]
# fruits4 = fruits[-3:-1]
# fruits5 = fruits[::-1]
# print(fruits2)
# print(fruits3)
# print(fruits4)
# print(fruits5)


# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key=len)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)

# 生成式和生成器
# f = [x for x in range(1, 10)]
# print(f)
# g = [x + y for x in 'ABCDE' for y in '123456']
# print(g)
# # 用列表的生成表达式语法创建列表容器
# # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
# h = [x ** 2 for x in range(1, 1000)]
# print(h)
# print(sys.getsizeof(h))  # 查看对象占用内存的字节数
# # 请注意下面的代码创建的不是一个列表而是一个生成器对象
# # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# j = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(j))  # 相比生成式生成器不占用存储数据的空间
# print(j)
# for val in j:
#     print(val)


# 定义元组
# t = ('骆昊', 38, True, '四川成都')
# print(t)
# print(t[0])
# print(t[3])
# for member in t:
#     print(member)

m = ('王大锤', 20, True, '云南昆明')
# 将元组转换成列表
person = list(m)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)














