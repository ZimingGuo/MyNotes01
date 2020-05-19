# author: Ziming Guo
# time: 2020/2/6
'''
练习2:
在控制台中录入，所有学生成绩.
输入空字符串，打印(一行一个)所有成绩.
打印最高分,打印最低分,打印平均分.
'''
# 我的方法1：
score_list = []
score_list_float = []
while True: # 用 while 语句的原因是：我也不知道要做几次
    score = input("请输入学生的成绩：")
    if score == "":
        break
    else:
        score_list.append(score)

for item in score_list:
    print(item)
    score_list_float.append(float(item))

print("最高分是："+str(max(score_list_float)))
print("最低分是："+str(min(score_list_float)))
print("平均分是："+str(sum(score_list_float) / len(score_list_float)))
# 通过上一个练习我学会了：
# 应该把录入成绩 和 打印成绩 这两件事分开来做
# 这样逻辑会清晰一些
# 不要把这两个部分都用 if 杂糅在一起哈！


# 我的方法2：
# score_list = []
# while True:
#     score = input("请输入学生的成绩：")
#     # 我终于发现了不能这么写的原因了：
#     #       当输入空字符串当时候，空字符串不能转换成浮点数
#     if score == "":
#         break
#     else:
#         score=float(score)
#         score_list.append(score)
#
# for item in score_list:
#     print(item)
#
# print(max(score_list))
# print(min(score_list))
# print(sum(score_list) / len(score_list))