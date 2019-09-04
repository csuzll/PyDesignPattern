"""
简单工厂模式: 集中式生产
"""

# 斧头: 产品抽象类
class Axe(object):
    def __init__(self, name):
        self.name = name

    def cutTree(self):
        print("%s斧头砍树" % self.name)

# 花岗岩石斧头: 子产品类
class StoneAxe(Axe):
    def cutTree(self):
        print("使用%s砍树" % self.name)

# 铁斧头: 子产品类
class SteelAxe(Axe):
    def cutTree(self):
        print("使用%s砍树" % self.name)

# 工厂类
class Factory(object):
    @staticmethod
    def create_axe(type):
        if type == "Stone":
            axe = StoneAxe("花岗岩斧头")
            return axe
        elif type == "Steel":
            axe = SteelAxe("铁斧头")
            return axe
        else:
            print("输入类型错误，没有此类型的斧头")

class Person(object):
    def __init__(self,name):
        self.name = name

    def work(self, axe_type):
        print("%s开始工作" % self.name)
        axe = Factory.create_axe(axe_type)
        axe.cutTree()

if __name__ == '__main__':

    p1 = Person("lili")
    p1.work("Steel")