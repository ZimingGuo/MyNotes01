# author: Ziming Guo
# time: 2020/4/11
'''
    demo04:
    flags 扩展功能演示
'''

import re

s = """Hello
北京
"""

# 只能匹配 ASCII 编码
# regex = re.compile(r'\w+') # 加上这个A就表示只能匹配ASCII码
# regex = re.compile(r'\w+', flags=re.A) # 加上这个A就表示只能匹配ASCII码

# 不区分大小写(应用：验证码)
# regex=re.compile(r'[a-z]+')
# regex=re.compile(r'[a-z]+',flags=re.I)

# .可以匹配换行
# regex=re.compile(r'.+') # 两处
# regex=re.compile(r'.+',flags=re.S) # 一处

# 匹配每一行的开头和结尾
# regex = re.compile(r'^北京')  # 匹配不到，因为只是第二行的开头
# regex = re.compile(r'^北京', flags=re.M)  # 可以匹配，M 就是这样用的

# 给正则表达式分行注释：
# regex = re.compile(r'\w+\s+\w+') # 把整个都匹配过来了
pattern = r"""\w+ # hello
\s+ # 匹配换行
\w+ # 北京
"""
regex = re.compile(pattern, flags=re.X | re.I)

l = regex.findall(s)
print(l)
