# author: Ziming Guo
# time: 2020/3/16
"""
    demo06：
        with.py
        使用with 打开文件
"""

with open('test.txt') as f:  # 生成文件对象f
    data = f.read()
    print(data)

# with语句块结束 f 自动销毁
