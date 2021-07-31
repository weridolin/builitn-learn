# -*- encoding: utf-8 -*-
import abc


class AbstractClass(abc.ABC):


    @abc.abstractmethod
    def test(self,method):
        """调用本地方法"""


    @abc.abstractmethod
    def add(self):
        """add method"""


    @abc.abstractmethod
    def sub(self):
        """subs method"""

class ChildClass(AbstractClass):
    """ 抽象类有的方法子类一定要实现"""

    def test(self,method):
        return getattr(self,method)


    def add(self):
        print("ADD")

# >>> c = ChildClass()
# >>> TypeError: Can't instantiate abstract class ChildClass with abstract methods add, sub


# 虚拟子类:不会从抽象类中继承任何方法OR属性
# isinstance(),issubclass()能识别
@AbstractClass.register
class VirturalClass(object):

    def test(self,method):
        return getattr(self,method)


    def add(self):
        print("ADD")

# >>> v = VirturalClass() 正常无报错
# 虚拟子类不会继承注册的抽象基类，而且任何时候都不会检 查它是否符合抽象基类的接口，即便在实例化时也不会检查。
# print(isinstance(VirturalClass(),AbstractClass)) >>> True
# print(issubclass(VirturalClass,AbstractClass))  >>> True


# __mro__:
# 即方法 解析顺序（Method Resolution Order）。
# 这个属性的作用很简单，按顺序 列出类及其超类，Python 会按照这个顺序搜索方法

class ClassA1():
    def test(self):
        print("classA1")

class ClassA2():
    def test(self):
        print("classA2")

class ClassA3(ClassA1,ClassA2):
    ...

class ClassA4(ClassA2,ClassA1):
    ...

# print(ClassA3.__mro__)
# (<class '__main__.ClassA3'>, <class '__main__.ClassA1'>, <class '__main__.ClassA2'>, <class 'object'>)
# ClassA3().test() # >>> classA1

# (<class '__main__.ClassA4'>, <class '__main__.ClassA2'>, <class '__main__.ClassA1'>, <class 'object'>)
# print(ClassA4.__mro__)
# ClassA4().test() # >>> classA2

# 列出所有子类列表
# print(AbstractClass.__subclasses__())

# 把内置类型 tuple、str、range 和 memoryview 注册为 Sequence 的 虚拟子类
# from typing import Sequence
# Sequence.register(tuple)
# Sequence.register(str)
# Sequence.register(range)
# Sequence.register(memoryview)
# # all ouput is true
# print(issubclass(tuple,Sequence))     >>> true
# print(issubclass(str,Sequence))       >>> true
# print(issubclass(range,Sequence))     >>> true
# print(issubclass(memoryview,Sequence))    >>> true
