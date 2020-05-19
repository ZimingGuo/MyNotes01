# author: Ziming Guo
# time: 2020/2/4
'''
练习5：
在控制台录入一个成绩，判断的等级
优秀/良好/及格/不及格/输入有误
'''
score = float(input("请输入一个成绩："))
if score > 100 or score < 0:
    print("输入成绩有误！")
elif score >= 90:
    print("成绩为优秀！")
elif score >= 80 : # 90 > score >= 80
    print("成绩为良好！")
elif score >= 60 : # 90 > score >= 60
    print("成绩为及格！")
else:
    print("成绩不及格，好好学学吧！")

# 在判断两个并列的条件 (用 and 连接) 的时候，可以直接用两个比较运算符完成，而不是 and
