# author: Ziming Guo
# time: 2020/2/9
'''
    练习3：
    在控制台中循环录入字符串，输入空字符停止.
    打印所有不重复的文字
'''
# 这道题如果用列表来做还是比较繁琐，还需要判断字符四否已经在列表里面
# 但是用集合做就特别好，自动排除重复元素
set01 = set()
while True:
    str01 = input("输入字符串：")
    if str01 == "":
        break
    set01.add(str01)
print(set01)
