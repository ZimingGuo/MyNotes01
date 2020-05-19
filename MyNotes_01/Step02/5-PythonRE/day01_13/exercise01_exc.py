# author: Ziming Guo
# time: 2020/4/12
'''
    练习：
    从 exc 文件里面寻找需要的字符
    即：编写接口函数，从终端输入端口名称
    获取端口运行状态中的地址值

    思路：
    1）根据输入的端口名称，找到对应的段落
    2）在该段落中匹配 address

    要知道怎么才能把输入的端口的那一段找出来，这属于文件读写的练习内容
    即：
'''

import re


def get_address(port):
    f = open('exc.txt', 'r')
    while True:
        # 通过这种方式获取一段内容
        data = ''  # 建立一个空的字符串，如果不是空行就会累加
        for line in f:  # 每次取一行
            if line == '\n':  # 遍历的内容是空行的话就跳出来
                break  # 因此，每当跳出循环之后就会得到一整段
            data += line  # 最后得到的结果就是一段内容
        if not data:  # 如果 data 为空说明到了文档结尾
            break

        # match 的作用就是匹配开始的位置
        # 用于检查这一段的开头是不是目标端口
        obj = re.match(port, data)  # 看是否能匹配到，匹配到了就会返回一个 match 对象

        # 如果 obj 不是空，就是要找的那一段
        # data 是目标段落
        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"  # 一共是三组，每一组四位数，表示十六进制，中间有三个.
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj01 = re.search(pattern, data)  # 目标字符串是 data，返回值是第一处符合的内容
            return obj01.group()  # 返回匹配到的内容
        # 如果为空，就循环回来继续找下一段

    return "没有该端口"


if __name__ == '__main__':
    port = input("端口:")
    print(get_address(port))
