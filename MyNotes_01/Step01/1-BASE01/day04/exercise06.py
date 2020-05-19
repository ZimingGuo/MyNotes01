# author: Ziming Guo
# time: 2020/2/5
"""
    练习6:
    随机加法考试
      随机产生两个数字(1--10),
      在控制台中获取两个数相加的结果
      如果用户输入正确得10分
    　总共３道题，最后输出得分.
    　例如:"请输入8+3=?"   10   不得分
    　　　　"请输入4+3=?"   7   得10分
    　　　　"请输入4+4=?"   8   得10分
          　”总分是20“
"""

import random
mark = 0

for i in range(0, 3):
    random_number_1 = random.randint(1, 10)
    random_number_2 = random.randint(1, 10)
    sum_computer = random_number_1 + random_number_2
    sum_customer = int(input(str(random_number_1)+ "+" + str(random_number_2) + "="))
    if sum_customer == sum_computer:
        print("加10分！")
        mark += 10
    else:
        print("不得分！")
print("总分是" + str(mark))
