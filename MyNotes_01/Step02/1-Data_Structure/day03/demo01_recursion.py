# author: Ziming Guo
# time: 2020/3/12
"""
demo01:
    求一个数的阶乘  n!
        1)像以前一样用 for 循环的思想
        2)用递归的方式实现
"""


def fun(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n - 1)


print(recursion(5))
