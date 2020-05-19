# author: Ziming Guo
# time: 2020/2/23
'''
    数据定义
'''
class StudentModel:
    """
    学生信息模型（模版）
    """

    def __init__(self, name="", age=0, score=0, id=0):
        # 正常来说这个 id 就不应该是人输入的，而应该是系统自动生成的，以保证准确性
        # 每次系统 add 一遍都会让 id 加一
        """
        创建学生对象
        :param id:编号(该学生的唯一标识)
        :param name:姓名(字符串类型)
        :param age:年龄 int
        :param score:成绩 float
        """
        self.__id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value