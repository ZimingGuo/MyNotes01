# author: Ziming Guo
# time: 2020/2/6
'''没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来
练习3：
在控制台中录入，所有学生姓名.
如果姓名重复，则提示"姓名已经存在",不添加到列表中.
如果录入空字符串，则倒叙打印所有学生.
没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来没调出来
'''
list_name = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    else:
        if name not in list_name: # pressure experience
                                  # 判断一个元素是否在容器里面
                                  # 不要用 for 遍历的方法，太麻烦
                                  # 用成员运算符很简便
            list_name.append(name)
        else:
            print("已经存在了！")

# 第一种倒序法宝：
for i in range(len(list_name)-1, -1, -1):
    print(list_name[i])

# 第二种倒序法宝：
for i in range(-1,-len(list_name)-1,-1):
    print(list_name[i])

# range()
# 如果里面是递增序列，最后写正步长，因为得一个个网上加
# 如果是递减序列，最后写负数，因为得一个个往下减
