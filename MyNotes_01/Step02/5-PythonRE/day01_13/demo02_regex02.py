# author: Ziming Guo
# time: 2020/4/11
'''
    demo02:
    re 模块 功能演示2
    生成 match 对象的函数
'''

import re

s = "今年是2019年，建国70周年"
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern, s)

for i in it:
    print(i.group())  # 每一次迭代出来的都是匹配出来的内容
    # 用 group() 可以获取 match 对象的内容

# 完全匹配一个字符串
# m = re.fullmatch(r'\w+', s)  # 没有完全匹配的话是要返回一个 none
# print(m.group()) # 这个会报错
n = re.fullmatch(r'[，\w]+', s)  # 没有完全匹配的话是要返回一个 none
print(n.group())

# 匹配开始位置
m=re.match(r'\w+',s) # 匹配不到，因为匹配的内容必须在开始位置
print(m.group())

# 匹配第一处符合正则表达式规则的内容
m=re.search(r'\d+',s) # 只能匹配第一个数字
print(m.group())
