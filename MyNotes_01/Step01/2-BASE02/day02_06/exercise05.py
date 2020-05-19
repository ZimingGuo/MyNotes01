# author: Ziming Guo
# time: 2020/2/8
'''
 练习5:
 在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
 如果名称输入空字符, 则停止录入.
 将所有信息逐行打印出来.

# 字典内嵌列表:
{ "张无忌":[28,100,"男"],}
'''
# 此题的结构是字典嵌套列表
# 字典内嵌列表 - 是一种很好的解决这类问题的方法
# 键是一个，列表是包括多个值的元组
dict_student = {}
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break

    list_student = []
    age = input("请输入学生年龄：")
    if age == "":
        break
    list_student.append(age)

    score = input("请输入学生成绩：")
    if score == "":
        break
    list_student.append(score)

    gender = input("请输入学生性别：")
    if gender == "":
        break
    list_student.append(gender)

    dict_student[name] = list_student

for k, v in dict_student.items():
    print_name = k
    # 下面三句话是分别从列表里面取出来东西
    print_age = v[0]
    print_score = v[1]
    print_gender = v[2]
    print("学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" % (print_name, print_age, print_score, print_gender))
