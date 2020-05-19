# author: Ziming Guo
# time: 2020/2/15
'''
    练习2：
        定义 在 list01 中查找name是"苏大强"的对象 的函数
        将名称与年龄在控制台中打印
'''


class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("第个学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" %
              (self.name, self.age, self.score, self.sex))  # 这句话就是在一次次访问(读取)实例变量


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("无极", 29, 70, "男"),
    Student("张三丰", 130, 96, "男")
]


def find_sdq():
    for item in list01:
        if item.name == "苏大强":
            return item  # 一定要清楚，此时return的是学生对象
    return None  # 这句话其实可以不写，因为如果没找到函数会自动返回空
    # 所以这个可以不写


# 测试代码
find_sdq().print_self_info()
print(find_sdq().name, find_sdq().age)


# 由此可以看出，类的好处是：用一个类型，封装了多个信息

# 练习：找所有女同学

def find_girl():
    list_girl = []
    for item in list01:
        if item.sex == "女":  # 判断完不能直接 return
            # 因为 return 之后就直接退出了，不能继续找了
            list_girl.append(item)
    return list_girl


# 测试代码
for item in find_girl():
    item.print_self_info()
print(find_girl()[0].name)


# 练习3：
# 定义函数：查找年龄在30岁以上，包括30岁的人的数量

def find_age_30above():
    list_age30 = []
    count = 0
    for item in list01:
        if item.age >= 30:
            list_age30.append(item)
            count += 1
    return list_age30, count


for item in find_age_30above()[0]:
    item.print_self_info()

print(find_age_30above()[1])


# 练习4：
#   定义函数：将 list01 中所有学生的成绩设置为零

def score_to_zero():
    for item in list01:
        item.score = 0
    return list01  # 其实不用写返回值，因为这个函数直接对列表进行操作
    # 这个函数把原来的列表给修改了，所以直接调出原来的列表就行


for item in score_to_zero():
    item.print_self_info()


# 练习5：
# 定义函数：获取 list01 中的所有学生的名字
def get_name():
    list_name = []
    for item in list01:
        list_name.append(item.name)
    return list_name


print(get_name())


# 练习6：
#   定义函数：查找年龄最大的人
def age_the_most():
    bigger_age_person = list01[0]
    for i in range(1, len(list01)):
        if bigger_age_person.age < list01[i].age:
            bigger_age_person = list01[i]
    return bigger_age_person


print(age_the_most().name)