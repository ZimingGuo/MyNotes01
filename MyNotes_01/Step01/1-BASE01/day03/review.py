# author: Ziming Guo
# time: 2020/2/3
'''
review.txt
'''
''' 短路逻辑 means 逻辑判断是尽量将复杂条件放在后面 '''
# 问题：控制台中会出现什么？
num = 1
re = num + 1 > 1 and input("请输入：") == "a"
# 答案：会出现 "请输入："
# 解析：只有 input & print 是能够让控制台里有显示的函数，原代码里面有 input，
# num + 1 > 1 这句话是 True，且两句话之间使用 and 连接，即使前一个是 True，也要判断后半句的 bool 状态
# 所以 input 才会出现在终端

# 问题：控制台中会出现什么？
num = 1
re = num > 1 and input("请输入：") == "a"
# 答案：什么也不会出现："
# 解析：虽然有 input 表示，但是前半句是 False，且中间是 and 连接
# and 连接的特点是，一旦有 False 就不用再判断后半句的状态了，直接判断完毕
# 所以 input 内容不会显示

# 启发：使用 and / or 判断条件时，复杂条件放在后面，这样一旦前面判断出结果，后面就不用再运行了。




print(1.2%4)