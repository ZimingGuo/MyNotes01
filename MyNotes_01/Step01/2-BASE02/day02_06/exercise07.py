# author: Ziming Guo
# time: 2020/2/9
'''
练习7：
     在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
     如果名称输入空字符, 则停止录入.
     将所有信息逐行打印出来.
'''
# 列表套字典的数据结构
#       一个大列表，里面很多个字典
#       每个字典里面包含录入的四个信息，用键值对一一对应
# 使用这种方式的原因是：他是有序的，可以灵活调用数据（索引）
list_student_info = []
while True:
    dict_student_info = {}

    name = input("请输入学生姓名：")
    if name == "":
        break
    dict_student_info["name"] = name

    age = input("请输入学生年龄：")
    if age == "":
        break
    dict_student_info["age"] = age

    score = input("请输入学生成绩：")
    if score == "":
        break
    dict_student_info["score"] = score

    gender = input("请输入学生性别：")
    if gender == "":
        break
    dict_student_info["gender"] = gender

    list_student_info.append(dict_student_info)
    # 注意往容器里面添加元素的方法，字典 & 列表是不同的

count = 0
for item in list_student_info:
    # 下面四句话是分别从列表里面取出来东西
    print_name = item["name"]
    print_age = item["age"]
    print_score = item["score"]
    print_gender = item["gender"]
    count += 1
    print("第%d个学生的姓名是%s,年龄是%s,成绩是%s,性别是%s" %
          (count, print_name, print_age, print_score, print_gender))

# 练习 5 6 7 分别用了三种数据结构
#   这是一种综合练习，以后在开发的过程中，工作中，经常是相互嵌套的
#   1）字典套列表
#   2）字典套字典
#   3）列表套字典
#   4）列表套列表
#   对比三种数据结构，每种方式特点不同，看练习仔细体会
#   想清楚选择策略！
