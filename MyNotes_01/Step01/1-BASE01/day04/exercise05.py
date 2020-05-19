# author: Ziming Guo
# time: 2020/2/5
'''
练习5：
1：累加1--100之间数的和 1+2+3+4...+100
2：累加1--100之间偶数的和 2+4+6+8+...+100
3：累加10--36之间数的和
'''

# 练习1：
sum_1 = 0 # 在循环外面开辟一块内存，存储这些累加之后的值
          # 这个变量就是用来存储累加和的
          # 随着数字的累加，sum 这个变量就会指向不同的值
for number_1 in range(1, 101):
    sum_1 += number_1
print(sum_1)

# 练习2：
sum_2 = 0
for number_2 in range(2, 101, 2):
    sum_2 += number_2
print(sum_2)

# 练习3：
sum_3 = 0
for number_3 in range(10, 37):
    sum_3 += number_3
print(sum_3)
