# author: Ziming Guo
# time: 2020/2/28
'''
    练习6：
    测试通用模块
'''
from common_my.list_helper_2 import *


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)
        # 加了这个方法之后就表示，之后在打印 item 的时候可以直接打印一个设定好的字符串了
        # 而不是打印看不懂的数据
        # 只要是加上这个 __str__ 方法，就表示打印字符串，而不是数据


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


def condition01(item):
    return item.atk_ratio > 6


def condition02(item):
    return 4 < item.duration < 11


def condition03(item):
    return len(item.name) > 4 and item.duration < 6


for item in ListHelper.find_all(list_skill, condition01):
    print(item)

# 经验：
# 把不变的提取到一个类中，把变化的提到一个模块里面

print("-------------------------------------------------------")


# 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
# 案例:查找名称是"葵花宝典"的技能.
#     查找编号是101的技能.
#     查找持续时间大于0的技能.

# 建议:
# 1. 现将所有功能实现
# 2. 封装变化(将变化点单独定义为函数)
#    定义不变的函数
# 3. 将不变的函数转移到list_helper.py中
# 4. 在当前模块测试

def condition_khbd(item):
    return item.name == "葵花宝典"


def condition_id101(item):
    return item.id == 101


def condition_duration_above0(item):
    return item.duration > 0


result01 = ListHelper.find_single_condition(list_skill, condition_khbd)
print(result01)

result02 = ListHelper.find_single_condition(list_skill, condition_id101)
print(result02)

result03 = ListHelper.find_single_condition(list_skill, condition_duration_above0)
print(result03)

# 在调用这种判断条件的函数的时候，给的参数虽然是个函数，但是不是让他执行的，所以是不要加括号
# 写在参数的位置只是为了把这个函数注入到上一级函数里面，进去之后再执行(写括号)

print("-------------------------------------------------------")

# 用 lambda 的形式完成上述练习
result04 = ListHelper.find_single_condition(list_skill, lambda item: item.name == "葵花宝典")
print(result04)

result05 = ListHelper.find_single_condition(list_skill, lambda item: item.id == 101)
print(result05)

result06 = ListHelper.find_single_condition(list_skill, lambda item: item.duration > 0)
print(result06)

print("-------------------------------------------------------")


# 需求1:计算技能列表中技能名称大于4个字的技能数量.
# 需求2:计算技能列表中技能持续时间小于等于5的技能数量.
# 步骤:
# 实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
# 将不变的函数提取到list_helper.py中


def condition_skill_name_above_4(element):
    return len(element.name) > 4


print(ListHelper.find_count_number(list_skill, condition_skill_name_above_4))


# 此时返回的是一个数值


def condition_duration_below_5(element):
    return element.duration <= 5


print(ListHelper.find_count_number(list_skill, condition_duration_below_5))
# 此时返回的是一个数值

print("-------------------------------------------------------")

# 用 lambda 改造

re07 = ListHelper.find_count_number(list_skill, lambda element: len(element.name) > 4)
print(re07)

re08 = ListHelper.find_count_number(list_skill, lambda element: element.duration <= 5)
print(re08)
