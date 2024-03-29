"""
单例模式
"""

#################################################################################
# class Singleton1(object):
#     """
#         单例实现方式一
#         通过重写__new__和__init__方法来改造对象的创建，从而实现单例模式
#     """
#     __instance = None # 类变量，存放类的对象
#     __isFirstInit = False # 确保只对类对象进行一次初始化

#     def __new__(cls, name):
#         if not cls.__instance:
#             Singleton1.__instance = super().__new__(cls)
#         return cls.__instance

#     def __init__(self, name):
#         if not self.__isFirstInit:
#             self.__name = name
#             Singleton1.__isFirstInit = True

#     def getName(self):
#         return self.__name

# # test
# tony = Singleton1("Tony")
# karry = Singleton1("Karry") # 将不会初始化
# print(tony.getName(), karry.getName())
# print("id(tony): ", id(tony), "id(karry): ", id(karry))
# print("tony == karry: ", tony == karry)


#################################################################################
# class Singleton2(type):
#     """
#         单例实现方式二
#         自定义 Singleton2 metaclass 
#     """

#     def __init__(cls, what, bases=None, dict=None):
#         super().__init__(what, bases, dict)
#         cls._instance = None # 初始化全局变量cls._instance为None

#     def __call__(cls, *args, **kwargs):
#         # 控制对象的创建过程，如果cls._instance为None则创建，否则直接返回
#         if cls._instance is None:
#             cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance

# class CustomClass(metaclass=Singleton2):
#     """用户自定义的类"""

#     def __init__(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

# # test
# tony = CustomClass("Tony")
# karry = CustomClass("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


#################################################################################
"""
    单例实现方式三
    装饰器的方法
"""
def singletonDecorator(cls, *args, **kwargs):
    """定义一个单例装饰器函数"""
    instance = {}

    # 包装函数
    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class Singleton3:
    """使用单例装饰器修饰一个类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

# # test
# tony = Singleton3("Tony")
# karry = Singleton3("Karry")
# print(tony.getName(), karry.getName())
# print("id(tony):", id(tony), "id(karry):", id(karry))
# print("tony == karry:", tony == karry)


# 模拟真爱
@singletonDecorator
class MyBeautifulGril(object):
    """我的漂亮女神"""

    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("遇见" + name + "，我一见钟情！")
        else:
            print("遇见" + name + "，我置若罔闻！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")

def TestLove():
    jenny = MyBeautifulGril("Jenny")
    jenny.showMyHeart()
    kimi = MyBeautifulGril("Kimi")
    kimi.showMyHeart()
    print("id(jenny):", id(jenny), " id(kimi):", id(kimi))

TestLove()
