# author: Ziming Guo
# time: 2020/2/24
"""
    练习3：
        定义函数，在控制台中获取成绩的函数.
        要求：1）如果异常，继续获取成绩，直到得到正确的成绩为止.
             2）成绩还必须在0--100之间，不在就直到得到正确的成绩为止.
"""


def get_score():
    score = float(input("请输入一个成绩："))
    if score > 100 or score < 0:
        raise ValueError
    elif score >= 90:
        print("成绩为优秀！")
    elif score >= 80:  # 90 > score >= 80
        print("成绩为良好！")
    elif score >= 60:  # 90 > score >= 60
        print("成绩为及格！")
    else:
        print("成绩不及格，好好学学吧！")


while True:
    try:
        get_score()
    except:
        continue
    else:
        print("成绩输入正确")

# # 老师答案更好：
# def get_score_01():
#
