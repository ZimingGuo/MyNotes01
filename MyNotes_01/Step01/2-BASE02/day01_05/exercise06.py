# author: Ziming Guo
# time: 2020/2/7
'''
练习6：
    在控制台中循环输入字符串，如果输入空则停止
    最后打印所有内容（拼接后的字符串）
'''
list01 = []
while True:
    str_temp = input("请输入字符串：")
    if str_temp != "":
        list01.append(str_temp)
    elif str_temp == "":
        str_whole = " ".join(list01)
        print(str_whole)
        break
# 这段程序的重点在于：以列表做为载体
# 在遇到面试题之后一定要这么写：先写成列表的形式，然后在转换成字符串

# 加一次 加两次 都可以用生成字符串的方法
# 但是如果加的次数大于三次，就要用列表了
