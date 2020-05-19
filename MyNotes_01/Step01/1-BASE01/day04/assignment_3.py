# author: Ziming Guo
# time: 2020/2/6
'''
作业3：
    按照以下格式，输出变量name = "悟空",age = 800,score = 99.5
    我叫xx,年龄是xx,成绩是xx。
'''
name = "悟空"
age = 800
score = 99.5
str01 = "我叫%s，年龄是%d，成绩是%.1f" % (name, age, score)
print(str01)
print("我叫%s，年龄是%d，成绩是%.1f" % (name, age, score))

# tips:
#   在用格式化的时候，注意要打印的内容的括号要和字符串连在一起，
#   组成一个东西，再把这个整体给 print，
#   而不是把要填充的东西放在 print 之外