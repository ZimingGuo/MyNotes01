# author: Ziming Guo
# time: 2020/2/9
'''
    demo02：
       集合
'''
# 1 创建集合
#   集合 ——> 字符串
set01 = set() # 创建空字符
set01 = set("abcac") # 创建带有默认值的字符
set02 = {"a", "b", "a"} # 创建带有默认值的字符
print(set01)
list01 = list(set01)
str01 = "".join(list01)  # 先把集合变列表，再把列表变成字符串
# 但是他有个缺点就是顺序变了，如果只是去重复可以这样做
print(str01)  # 这时候的字符串是有括号的
print(list01)
#   创建具有默认值的集合
print(set02)

# 2 添加元素
set01.add("qtx")

# 3 删除元素
set02.remove("a")

# 4 获取所有元素
for item in set02:
    print(item)

# 5 数学运算
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集
print(set01 & set02)  # {2,3} 这个执行完得到的还是个集合

# 并集
print(set01 | set02)  # {1,2,3,4}

# 补集
print(set01 ^ set02)  # {1,4}
print(set01 - set02) # 表示的是set01里面有但是set02里面没有的
                     # 类似单侧补集
                     # 补集就是找不同

# 子集
set03 = {1, 2}  # 我有的你都有
print(set03 < set01)

# 超集
print(set01 > set03)
