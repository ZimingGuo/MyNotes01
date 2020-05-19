# author: Ziming Guo
# time: 2020/2/27
"""
    练习4：
    参照day10/exercise02.py
    完成下列练习
"""


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成

# 生成器函数
def get_atk_above_6(list_target):
    for item in list_target:
        if item.atk_ratio > 6:
            yield item.name


result01 = get_atk_above_6(list_skill)
for item in result01:
    print(item)

# 生成器表达式
result02 = (item for item in list_skill if item.atk_ratio > 6)
for item in result02:
    print(item.name)


# 练习2:获取持续时间在4--11之间的所有技能

# 生成器函数
def get_duration_above_6(list_target):
    for item in list_target:
        if item.duration > 4 and item.duration < 11:
            yield item.name


result03 = get_duration_above_6(list_skill)
for item in result03:
    print(item)

# 生成器表达式
result04 = (item for item in list_skill if item.duration > 4 and item.duration < 11)
for item in result04:
    print(item.name)


# 练习3:获取技能编号是102的技能
# 生成器函数
def get_102(list_target):
    for item in list_target:
        if item.id == 102:
            yield item


result05 = get_102(list_skill)
for item in result05:
    print(item)

# 生成器表达式
result06 = (item for item in list_skill if item.id == 102)
for item in result06:
    print(item)


# 练习4:获取技能名称大于4个字并且持续时间小于6的所有技能
# 生成器函数
def get_double_condition(list_target):
    for item in list_target:
        if item.duration < 6 and len(item.name) > 4:
            yield item


result07 = get_double_condition(list_skill)
for item in result07:
    print(item)

# 生成器表达式
result08 = (item for item in list_skill if item.duration < 6 and len(item.name) > 4)
for item in result08:
    print(item)
