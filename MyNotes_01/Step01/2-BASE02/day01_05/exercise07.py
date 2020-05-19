# author: Ziming Guo
# time: 2020/2/7
'''
练习7：
英文单词反转
"How are you" ——> "you are How"
'''
str01 = "How are you"
list01 = str01.split(" ") # 拆分完的结果是个列表
list02 = []

for i in range(len(list01) - 1, -1, -1):
    list02.append(list01[i])

str02 = " ".join(list02) # 列表再变成字符串
print(str02)

# 思想：先由字符串转换成列表，因为列表可变，比较灵湖，所以先转换成列表进行倒序
#      然后在以空格为连字符，转换回字符串。
