# author: Ziming Guo
# time: 2020/4/11
'''
    demo01：
    re 模块
    功能演示
'''

import re  # 标准库模块，不用在安装

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+"  # 正则表达式(无子组)

# 方法1：re模块直接调用 findall
# findall 返回值是一个列表
l = re.findall(pattern, s)  # 结果就是匹配两处
print(l)

# 用 compile 对象调用 findall
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)

# 按照正则表达式匹配内容切割字符串： split
l = re.split(r'[:,]', s)  # 建立一个字符集，字符集里面是冒号和逗号，就是按照:和,进行切割
print(l)

# 替换目标字符串
s = re.sub(r':', '-', s, 1)
print(s)
