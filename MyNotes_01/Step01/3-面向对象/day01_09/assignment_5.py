# author: Ziming Guo
# time: 2020/2/13
'''
    作业5：
    以万物皆对象的思想，洞察客观实物，
    随意创建两个类，四个对象，并调用其方法.
'''


# 创建的第一个类
class Coffee_Bean:
    # 数据成员
    def __init__(self, name, origin, taste):
        self.name = name
        self.origin = origin
        self.taste = taste

    # 行为成员
    def brew(self):
        """
        冲咖啡
        """
        print(self.name + "可以手冲，他的原产地是" + self.origin + "，味道是" + self.taste)


# 创建对象（其实是调用了 __init__ 方法）
c01 = Coffee_Bean("曼特宁", "哥伦比亚", "焦糖")  # 创建对象的时候用到了数据成员的方法

# 调用对象的行为
c01.brew()  # 调用对象的时候用到了行为成员的方法


# 创建的第二个类
class Camera:
    # 数据成员
    def __init__(self, brand, type, focal_length):
        self.brand = brand
        self.type = type
        self.focal_length = focal_length

    # 行为成员
    def shooting(self):
        """
        拍照片
        """
        print(self.brand + "的" + self.type + "相机有很多焦段：" + self.focal_length)

# 创建对象
c02 = Camera("索尼", "微单", "18-135")

# 调用对象的行为
c02.shooting()
