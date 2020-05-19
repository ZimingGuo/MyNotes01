# author: Ziming Guo
# time: 2020/2/5
'''
练习4：
像上次那个练习一样录入成绩
循环根据成绩判断登等级，如果录入空字符串则退出程序
如果成绩录入次数到达3，则退出并提示"成绩错误过多"
'''
count = 0
while count < 3:
    score = input("请输入一个成绩：")
    if score == " ":
        print("格式不正确！")
        break # 不会执行 else 语句
    elif float(score) > 100 or float(score) < 0:
        print("输入成绩范围有误！")
        count += 1
    elif float(score) >= 90:
        print("成绩为优秀！")
    elif float(score) >= 80:
        print("成绩为良好！")
    elif float(score) >= 60:
        print("成绩为及格！")
    else:
        print("成绩不及格，好好学学吧！")
else:
    print("错误次数过多！")

# 几个tips哈：
# 1）转换数据类型的符号（int float str...）不一定要放在input之后
#    这样可能会造成获取数据的类型的限制
# 2）计数器设置好之后不一定要放在循环的开头 or 结尾
#    可以根据需要，把计数器放在所要计数的条件的前后
# 3）while 循环里面的 break 的作用是直接跳出循环
#    跳出循环之后，不会进入 else 里面
#    但是如果是不满足 while 后面的条件而退出，则进入 else ，执行相应语句
# 总结：
# break 是条件满足退出的方式 ；else 是条件不满足退出的方式
#  也正因为 while 语句中 break 和 else 的这个特点
#  我们可以通过结果知道程序是从哪里退出来的！
