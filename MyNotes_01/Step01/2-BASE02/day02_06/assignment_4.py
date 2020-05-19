# author: Ziming Guo
# time: 2020/2/9
'''
作业4：
    存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
      　北京：
            景区：故宫,天安门,天坛.
            美食: 烤鸭,炸酱面,豆汁,卤煮.
        四川:
            景区：九寨沟,峨眉山,春熙路．
            美食: 火锅,串串香,兔头.
# 找一个自己认为适合的数据结构来做
'''
whole = \
    {
        "北京": {"景区": ["故宫", "天安门", "天坛"], "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]},
        "四川": {"景区": ["九寨沟", "峨眉山", "春熙路"], "美食": ["火锅", "串串香", "兔头"]}
    }

for province, content in whole.items():
    scenery = content["景区"]
    food = content["美食"]
    print("%s的景区有：%s，美食有：%s" % (province, scenery, food))

# 获取四川所有美食：
print(whole["四川"]["美食"])

# 获取所有城市：(就是获取所有键)
for item in whole:
    print(item)

# 获取所有城市的所有景区
list02 = []
for key in whole:
    for item in whole[key]["景区"]:
        list02.append(key + ":" + item)
print(list02)

# 在列表里获取键：直接 for item in dict：就可以
# 在列表里获取值：for item in dict.values:
# 在列表里获取键值：for item in dict.items: 这样里面就是以元组构成的键值对
