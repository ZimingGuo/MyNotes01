# author: Ziming Guo
# time: 2020/2/6
"""
    练习１：
    在控制台中录入，西游记中你喜欢的人物.
    输入空字符串，打印(一行一个)所有人物.
"""
list_xyj=[] # 先建一个列表
count=0

while True:
    character=input("请输入喜欢的人物:")
    if character=="":
        for item in list_xyj:
            print(item)
        break
    else:
        list_xyj.append(character)

# 在这里更正一下：
#   while True 这个语句，如果里面有 if else 语句
#   即使不满足 if 后面的内容而进到了 else 里面
#   也不会返回 False 值而退出 while True 这个循环
#   这个循环只能由 break 退出来
#   可以考虑在 else 语句执行之后加一个 break


# 老师的方法：分两步
#           1）录入名字
#           2）打印
while True:
    character=input("请输入喜欢的人物:")
    if character =="":
        break
    else:
        list_xyj.append(character)

for item in list_xyj:
    print(item)
# 老师的方法 好在把存储名字的过程和打印的过程分开了


