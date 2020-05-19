# author: Ziming Guo
# time: 2020/3/15
'''
    练习4：
        从终端输入一个单词，在单词本上找到这个单词
        解释这个单词
        如果找不到，就打印找不到
'''
dict = open('dict.txt', 'r')

voca = input("请输入要查找的单词：")
list_dict = dict.readlines()

for item in list_dict:
    voca_target = item.split(" ")[0]  # 以空格为界将元素分割，第一个元素就是要找的单词
    if voca_target > voca:  # 这句话就是防止，即使没有这个单词，还要遍历一整遍列表的情况
        break
    if voca == voca_target:
        print(item)
        break
else:  # 要注意：这个 else 执行的条件是，所有的 for 循环都已经运行结束了，没有执行 break
    print("此单词不存在！")

dict.close()

# 总结经验：想要分隔单词和释义，一定要想到 split 这个函数
