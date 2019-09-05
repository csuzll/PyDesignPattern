"""迭代器模式"""

class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """将指针移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """将指针移至结尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "移动至上一个元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        if (self.__curIdx < len(self.__data) and self.__curIdx >= 0):
            return self.__data[self.__curIdx]
        else:
            return None

def testBaseIterator():
    print("从前往后遍历:")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer, end="\t")
    print()

    print("从后往前遍历:")
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print(customer, end="\t")

testBaseIterator()


#  方法一：使用()定义生成器
gen = (x * x for x in range(10))

#  方法二：使用yield定义generator函数
def fibonacci(maxNum):
    """斐波那契数列的生成器"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b

def testIterable():
    print("方法一，0-9的平方数：")
    for e in gen:
        print(e, end="\t")
    print()

    print("方法二，斐波那契数列：")
    fib = fibonacci(10)
    for n in fib:
        print(n, end="\t")
    print()

    print("内置容器的for循环：")
    arr = [x * x for x in range(10)]
    for e in arr:
        print(e, end="\t")
    print()

    print()
    print(type(gen))
    print(type(fib))
    print(type(arr))

testIterable()

class NumberSequence:
    """生成一个间隔为step的数字系列"""

    def __init__(self, init, step, max = 100):
        self.__data = init
        self.__step = step
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        if(self.__data < self.__max):
            tmp = self.__data
            self.__data += self.__step
            return tmp
        else:
            raise StopIteration

def testNumberSequence():
    numSeq = NumberSequence(0, 5, 20)
    print(isinstance(numSeq, Iterable))
    print(isinstance(numSeq, Iterator))
    for n in numSeq:
        print(n, end="\t")

testNumberSequence()