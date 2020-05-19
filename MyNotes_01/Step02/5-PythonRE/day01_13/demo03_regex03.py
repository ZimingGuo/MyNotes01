# author: Ziming Guo
# time: 2020/4/11
'''
    demo3：regex3
    match 对象属性演示
'''

import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
obj = regex.search('abcdefghi', 0, 8)  # 有了 match 对象，此时也可以直接传一个开始和结尾
# 后两个参数的意思是，截取目标字符串的一部分，作为匹配对象

# 属性变量
print(obj.pos)  # 匹配目标字符串的开始位置
print(obj.endpos)  # 匹配目标字符串的结尾位置
print(obj.re) # 正则表达式
print(obj.string) # 全部目标字符串内容，并不是截取配对出来的内容
print(obj.lastgroup) # 最后一组的组名，如果最后一组没有组名，就会返回一个none
print(obj.lastindex) # 最后一组的组号（序列号）

print("==========================================================")
# 属性方法（无方法，直接打印）
print(obj.span()) # 匹配内容在字符串中的位置-起始位置
print(obj.start()) # 匹配内容在字符串中的位置-开始位置
print(obj.end()) # 匹配内容在字符串中的位置-结束位置
print(obj.groupdict()) # 生成捕获组和其对应内容的字典
print(obj.groups()) # 把所有子组的匹配内容生成一个元组

# 获取 match 对象对应的内容
print(obj.group()) # 表示每一个子组对应的内容，括号里默认是全部子组，可以填写组号


