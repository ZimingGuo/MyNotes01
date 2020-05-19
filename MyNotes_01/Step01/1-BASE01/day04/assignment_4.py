# author: Ziming Guo
# time: 2020/2/6
'''
作业4：
    在控制台中获取一个整数作为边长．
    　　根据边长打印矩形．
       例如：４
           ****
           *  *
           *  *
           ****

           6
           ******
           *    *
           *    *
           *    *
           *    *
           ******
'''

rec_len=int(input("请输入矩形的边长："))
down=up="*"*rec_len # 表示上下边长
middle=" "*(rec_len-2) # 表示中间部分，每一行里，空格的部分
left="*%s*"%(middle) # 表示中间部分，每一行里，两端的星号

print(up) # 打印上边

# 打印中间部分
for item in range(1,rec_len-1):
    print(left)

print(down) # 打印下边
