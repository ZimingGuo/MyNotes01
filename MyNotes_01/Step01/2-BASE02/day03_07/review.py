# author: Ziming Guo
# time: 2020/2/9
"""
    day06 复习
    容器
        字符串: 不可变 存储编码值 序列
        列表: 可变　存储变量 序列
             预留空间
             扩容：开辟更大的空间
                 拷贝原有数据
                 替换引用
        元组:不可变　存储变量　序列
            按需分配
        字典:可变 存储键值对 散列
        集合:可变 存储键 散列
        固定集合:不可变 存储键 散列
"""
list01 = []
list01 = ["qtx", "xz", "jd"]
list01.append("mm")
list01.insert(1, "wt")

# item 变量指向列表中的元素
for item in list01:
    print(item)

# 变量 i 表示索引
# 这个方法更加灵活
for i in range(len(list01)):
    print(i)

# 修改
# 先用索引定位
list01[0] = "QTX"

# 删除
list01.remove("mm")

dict01 = {"qtx": 100, "xz": 65, "jd": 85}
dict01["mm"] = 95
# 获取所有元素
for key in dict01:
    print(key)
    print(dict01[key])

for value in dict01.values():
    print(value)

for key, value in dict01.items():
    print(key)
    print(value)

# 修改
# 字典是靠键来定位的
dict01["qtx"] = 101

# 删除
# 根据键定位
del dict01["mm"]

list02 = ["看书", "编程"]
dict02 = {"qtx": list02}
list02.append("听音乐")
print(dict02)