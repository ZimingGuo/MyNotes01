# author: Ziming Guo
# time: 2020/2/9
'''
    练习6：
     在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
     如果名称输入空字符, 则停止录入.
     将所有信息逐行打印出来.
'''
# 条件：要字典嵌套字典的数据结构
dict_student_key = {}
while True:
    dict_student_value = {}
    name = input("请输入学生姓名：")
    if name == "":
        break

    age = input("请输入学生年龄：")
    if age == "":
        break
    dict_student_value["age"] = age

    score = input("请输入学生成绩：")
    if score == "":
        break
    dict_student_value["score"] = score

    gender = input("请输入学生性别：")
    if gender == "":
        break
    dict_student_value["gender"] = gender

    dict_student_key[name] = dict_student_value

for k, v in dict_student_key.items():
    print_name = k
    # 下面三句话是分别从列表里面取出来东西
    print_age = v["age"]
    print_score = v["score"]
    print_gender = v["gender"]
    print("学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" %
          (k, print_age, print_score, print_gender))

# 因为字典是无序的，
# 所以使用字典的时候，虽然读取的速度快了，但是灵活性大大降低了
# 例如：不能够读取最后一个人的信息，因为是无序的