"""命令模式"""

# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    """命令的抽象类"""

    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    """命令的具体实现类"""

    # 与接收者绑定在一起
    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.doSomething()

class Receiver(object):
    """命令的接收者"""

    def doSomething(self):
        print("do something...")

class Invoker:
    """调度者"""

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def action(self):
        if self.__command is not None:
            self.__command.execute()

if __name__ == '__main__':
    def client():
        invoker = Invoker() # 调度者
        command = CommandImpl(Receiver()) # 绑定接收者的命令
        invoker.setCommand(command) # 调度者接收命令
        invoker.action() # 接收者执行命令

    client()
