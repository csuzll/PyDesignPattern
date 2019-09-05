"""模板方法模式"""
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ReaderView(metaclass=ABCMeta):
    """阅读器视图（模板类）"""

    def __init__(self):
        self.__curPageNum = 1

    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum) + "的内容"

    def prePage(self):
        """模板方法，往前翻一页"""
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        """模板方法，往后翻一页"""
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        """翻页效果（模板方法）"""
        pass

class SmoothView(ReaderView):
    """左右平滑的视图（模板实现类1）"""

    def _displayPage(self, content):
        print("左右平滑:" + content)

class SimulationView(ReaderView):
    """仿真翻页的视图（模板实现类2）"""

    def _displayPage(self, content):
        print("仿真翻页:" + content)

def testReader():
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()

testReader()