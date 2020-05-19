# author: Ziming Guo
# time: 2020/2/8
'''
    demo01
    列表推导式
'''
# 需求：将 list01 里面的所有元素，增加1以后存入 list02 中
list01 = [5, 56, 6, 7, 7, 8, 19]
# list02 = []
# for item in list01:
#     list02.append(item + 1)

#   上面的这段代码所表达的意思可以这样写：
list02 = [item + 1 for item in list01]
print(list02)


# 需求：将 list01 里面大于10的元素，增加1以后存入 list02 中
# list02 = []
# for item in list01:
#     if item > 10:
#         list02.append(item + 1)
#    上面的这段代码所表达的意思可以这样写：
list02 = [item + 1 for item in list01 if item > 10]
print(list02)
