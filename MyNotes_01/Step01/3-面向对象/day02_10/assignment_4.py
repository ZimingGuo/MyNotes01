# author: Ziming Guo
# time: 2020/2/15
'''
    定义敌人类
        --　数据:姓名,血量,基础攻击力,防御力
        --　行为:打印个人信息

       创建敌人列表(至少４个元素),并画出内存图。
       查找姓名是"灭霸"的敌人对象
       查找所有死亡的敌人
       计算所有敌人的平均攻击力
       删除防御力小于10的敌人
       将所有敌人攻击力增加50
'''


class Enemy():
    count = 0

    def __init__(self, name, blood, capacity, defense):
        self.name = name
        self.blood = blood
        self.capacity = capacity
        self.defense = defense

    def print_info(self):
        print("名字：%s ""血量：%s ""基础攻击力：%s ""防御力：%s " % (self.name, self.blood, self.capacity, self.defense))


# 创建了一个对象列表
list_enemy = [
    Enemy("灭霸", 100, 99, 98),
    Enemy("大黄蜂", 0, 80, 9),
    Enemy("擎天柱", 100, 90, 90),
    Enemy("威震天", 100, 89, 95),
    Enemy("霸天虎", 100, 91, 85)
]

# 1
for item in list_enemy:
    if item.name == "灭霸":
        item.print_info()

# 2
for item in list_enemy:
    if item.blood == 0:
        item.print_info()

# 3
count = 0
attack01 = 0
for item in list_enemy:
    count += 1
    attack01 += item.capacity
average_attack = attack01 / count
print(average_attack)

# 4
# 注意注意 涉及到列表里元素的删除 一定要倒着删除
# 倒着删除的原因是：如果正序，一边删除，一边遍历向前，就会错过元素
for i in range(len(list_enemy) - 1, -1, -1):
    if list_enemy[i].defense < 10:
        # list_enemy.remove(list_enemy[i])
        del list_enemy[i]

# for item in list_enemy:
#     if item.defense < 10:
#         # del item
#         list_enemy.remove(item)

for item in list_enemy:
    item.print_info()

# 5
for item in list_enemy:
    item.capacity += 50

for item in list_enemy:
    item.print_info()
