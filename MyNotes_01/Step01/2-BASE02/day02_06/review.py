# author: Ziming Guo
# time: 2020/2/8
"""
    day05 复习
    容器
        通用操作
        字符串:不可变　　存储编码值　　序列
        列表:可变　　存储变量　　　　　序列
            基础操作
                1.创建:[数据]   list(容器)
                2.定位：索引　　切片
                    # 从列表中获取一片元素组成新列表
                    变量 = 列表名[切片]
                    # 修改一片元素
                    列表名[切片] = 变量
                3.删除:
                    del 列表名[索引/切片] 索引就删一个 切片就删一片
                    列表名.remove(元素)
                    从列表中删除 "多个" 元素,建议倒序删除. # ！倒序倒序！
                4.增加:
                    列表名.append(元素)
                    列表名.insert(索引,元素)
                5. 遍历所有元素
                    下列代码
"""
# 遍历所有元素
list01 = [3, 4, 4, 5, 6]
# 打印列表，而不是把元素一个个都拿出
# print(list01)
# 正向
for item in list01:
    print(item)

# 倒序的方式：！不建议不建议！
for item in list01[::-1]:
    print(item)

# 反向(索引)
# 3  2  1  0
for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

# -1 -2 -3 -4
for i in range(-1, -len(list01) - 1, -1):
    print(list01[i])