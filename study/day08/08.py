# def foo():
#     print('hello, world!')
# foo()
# def foo():
#     print('goodbye, world!')
# foo()

#
# from module1 import foo
# foo()
#
# from module2 import foo
# foo()

#
# import module1 as m1
# import module2 as m2
# m1.foo()
# m2.foo()


#
# from module1 import foo
# from module2 import foo
# # 输出goodbye, world!
# foo()



#
# def foo():
#     pass
#
#
# def bar():
#     pass
#
#
# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()


# 实现计算求最大公约数和最小公倍数的函数。
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)











