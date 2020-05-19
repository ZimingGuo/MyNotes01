# author: Ziming Guo
# time: 2020/3/8
"""
    练习1_edited：
        逆波兰表达式实现
"""

from demo01_sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')
    # 按照空格切割字符串
    # 这个逆波兰表达式的实现的精髓也就在于此，一定要把整个的这个字符串转换成列表
    for i in tmp:
        if i not in ['+', '-', '*', '/', 'p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y) # 直接 push 进去，不用先拿出来
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.top())
