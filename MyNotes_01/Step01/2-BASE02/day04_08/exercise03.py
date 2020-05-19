# author: Ziming Guo
# time: 2020/2/10
'''
    练习3：
    定义 根据成绩计算等级 的函数
'''

# def rank_based_on_score(score):
#     """
#     根据学生成绩划分成绩等级
#     :param score: 分数 float
#     :return: 等级（0——4：输入错误 优 良 及 不及）
#     """
#     if score > 100 or score < 0:
#         return "成绩输入有误"
#     elif score >= 90:
#         return "优秀"
#     elif score >= 80:
#         return "良好"
#     elif score >= 60:
#         return "及格"
#     else:
#         return "不及格"


# print("学生成绩等级为：%d" % (rank_based_on_score(98)))

def rank_based_on_score(score):
    """
    根据学生成绩划分成绩等级
    :param score: 分数 float
    :return: 等级（0——4：输入错误 优 良 及 不及）
    """
    if score > 100 or score < 0:
        return "成绩输入有误"
    if score >= 90:  # 之前这里用 elif 是因为互斥性
                       # (不满足上面的条件的时候满足这条)
                       # 但是此时，由于有了 return 直接就能退出方法，所以 elif 的互斥性没用了
                       # 所以直接改成 if 就可以
        return "优秀"
    if score >= 80:
        return "良好"
    if score >= 60:
        return "及格"
    return "不及格"

print("学生成绩等级为：%s" % (rank_based_on_score(98)))
