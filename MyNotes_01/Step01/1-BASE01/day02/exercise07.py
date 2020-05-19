# author: Ziming Guo
# time: 2020/2/3
'''
练习7：判断是否为闰年
闰年：True 年份能被4整除，但是不能被100整除；或者年份能被400整除
平年：False
'''
'''我的方法：有点笨'''
# year = int(input("请输入一个年份："))
# # 能被4整除：
# result_4 = not year % 4
# # 能被100整除：
# result_100 = not year % 100
# # 能被400整除：
# result_400 = not year % 400
#
# result_final = (result_4 and (not result_100)) or (result_400)
# print("输入年份是否为闰年？" + str(result_final))

'''老师的方法：'''
year = int(input("请输入一个年份："))
# 能被4整除：
divided_4 = year % 4 == 0
# 不能被100整除：
not_divided_100 = year % 100 != 0
# 能被400整除：
divided_400 = year % 400 == 0

final_result = (divided_4 and not_divided_100) or (divided_400)
print("输入年份是否为闰年？" + str(final_result))

# Drafts:
# 能被4整除 and 能被100整除 false
# 不能被4整除 and 能被100整除 false
# 不能被4整除 and 不能被100整除 false
# 能被4整除 and 不能被100整除 true


