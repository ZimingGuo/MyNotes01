# author: Ziming Guo
# time: 2020/2/7
'''
    demo03
'''
# 需求：根据 XXX 逻辑，拼接一个字符串
# "0123456789"
result=""
for item in range(10):
    # ""
    # "0"
    # "01"
    # "012" 每次都会生成一个新的字符串
    # 实际上就是每次都生成一个新的字符串，然后 result 指向这个新的字符串
    result += str(item)
print(result)
# 缺点：这种方式，每一次拼接都会生成一个新的字符串，划不来


# 另一种方法：
# 可以先建立一个列表，然后把东西逐次放列表
list_temp=[]
for item in range(10):
    list_temp.append(str(list_temp))

result = "".join(list_temp)
# join 函数就是可以把列表变成字符串
# join 前面的双引号里面应该填连接符，每个字符串之间的连接符
print(type(result)) # type函数可以用来查看类型
print(result)
# 这些操作就不会每次都新建一个新的列表，而是往列表里不断加字符串