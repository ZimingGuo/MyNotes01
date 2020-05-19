# author: Ziming Guo
# time: 2020/3/8
'''
    练习1 :
        利用顺序栈,完成逆波兰表达式的执行演示过程
        想清楚逆波兰运算过程的原理，各个数据是怎么样在栈里面移动的
'''
from demo01_sstack import *

sstack01 = SStack()

str01 = input()
'''
for item in str01:
    if int(item):
        sstack01.push(int(item))
    else:
        target01 = sstack01.pop()
        target02 = sstack01.pop()
        if item == "+":
            result = target01 + target02
            sstack01.push(result)
        elif item == "-":
            result = target02 - target01
            sstack01.push(result)
        elif item == "*":
            result = target01 * target02
            sstack01.push(result)
        elif item == "/":
            result = target02 / target01
            sstack01.push(result)
        elif item == "//":
            result = target02 // target01
            sstack01.push(result)
        elif item == "%":
            result = target02 % target01
            sstack01.push(result)
'''

for i in range(len(str01)):
    if str01[i] == "p":
        print(sstack01.top())
    elif i == 0 or i % 2 == 1:
        sstack01.push(int(str01[i]))
    else:
        target01 = sstack01.pop()
        target02 = sstack01.pop()
        if str01[i] == "+":
            result = target01 + target02
            sstack01.push(result)
        elif str01[i] == "-":
            result = target02 - target01
            sstack01.push(result)
        elif str01[i] == "*":
            result = target01 * target02
            sstack01.push(result)
        elif str01[i] == "/":
            result = target02 / target01
            sstack01.push(result)
        elif str01[i] == "//":
            result = target02 // target01
            sstack01.push(result)
        elif str01[i] == "%":
            result = target02 % target01
            sstack01.push(result)
