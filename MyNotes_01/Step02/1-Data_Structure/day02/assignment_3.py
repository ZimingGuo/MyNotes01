# author: Ziming Guo
# time: 2020/3/10
'''
    作业3：
        编程作业：
            编写一个接口程序，获取一段文字
            判定文字中括号是否匹配
            如果正确则打印 "正确"
            不正确就指出出错的地方
'''

from demo01_sstack import *
from demo02_lstack import *

content = input("请输入一段内容：")
st01 = SStack()

# 首先需要把获取来的字符串打散，方法如下：
# 符号都是英文下的符号
list_temp = content.split(" ")  # 这段程序的问题是：字符分割出现了问题

for item in list_temp:
    if item in ["(", "{", "["]:
        st01.push(item)  # 如果是以上符号就压栈
    elif item == ")":
        check01 = st01.pop()
        if check01 == "(":
            pass
        else:
            print('"("处出现了错误！')
            break
    elif item == "}":
        check02 = st01.pop()
        if check02 == "{":
            pass
        else:
            print('"}"处出现了错误！')
            break
    elif item == "]":
        check03 = st01.pop()
        if check03 == "[":
            pass
        else:
            print('"]"处出现了错误！')
            break
else:
    print("全部正确")
