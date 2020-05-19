# author: Ziming Guo
# time: 2020/2/10
'''
    练习6:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
'''
list01 = [3, 80, 45, 5, 81, 1]

result = False  # 这句话就是做了一个标记！！！很 nice
for m in range(len(list01) - 1):

    for i in range(m + 1, len(list01)):
        if list01[m] == list01[i]:
            print("具有相同项")
            result = True  # 如果程序执行到了这里，result就会改编成 True ，就不会打印后面那句话
            break
    if result == True:
        break

if result == False:
    print("没有相同项")

# 经验：
#   如果在一段具有两个循环的程序里像退出程序，就要加上标记
#   加上标记是一个很实用的编程方式
