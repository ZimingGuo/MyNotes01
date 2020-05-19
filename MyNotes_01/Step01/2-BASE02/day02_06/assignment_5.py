# author: Ziming Guo
# time: 2020/2/9
'''没调出来没调出来没调出来没调出来没调出来没调出来没调出来
作业5：
    计算一个字符串中的字符出现的次数.
    # 思想：
    # 逐一判断字符出现的次数.
    # 如果统计过则增加１，如果没统计过则等于１.

    abcdefce
    a 1
    b 1
    c 2
    d 1
    e 2
    f 1
没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没
'''
# 我的想法：
#   建立一个列表，键为字符(str)，值为出现的次数(int)
dict_times = {}
str01 = input("请输入一个字符串：")
list01 = list(str01)
# 上面这个思想是对的，键值对来匹配字符串和次数
# 方法是：
for item in list01:
    if item in dict_times:
        dict_times[item] += 1  # 这句代码的精髓在于：
    elif item not in dict_times:
        dict_times[item] = 1
    #   直接在 value 的变量里面加一，然后就存储在值里面了

# for i1 in range(0, len(list01)):
#     count = 1
#     i2 = i1 + 1
#     while i2 < len(list01) - 1:
#         if list01[i1] == list01[i2]:
#             count += 1
#             list01.remove(list01[i2])
#         i2 += 1
#     dict_times[list01[i1]] = count
# 我的这个方法太麻烦了，而且还做不出来
#   我的这个方法笨就笨在非要用 count 来计数
#   再把count奇数出来的值放进字典
#   用了两步，而且还没有体现出字典的优势

for k, v in dict_times.items():
    print("%s出现的次数为：%s" % (k, v))
