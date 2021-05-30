# -*- encoding: utf-8 -*-

# https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3

# 一句话 类变量---> 所有实例共享的变量     类方法---->所有实例共享的方法

class Test(object):
    cls_Var1 = "this is class variable"

    def __init__(self):
        self.i_var = "sss"


T = Test()
T.cls_Var1 = 22  # 这个地方其实实例里面又创建了一个新的变量cls_Var1
print(Test.cls_Var1)

Test.cls_Var1 = "22"  # 这才是改了类变量的值的正确方式
print(Test.cls_Var1)

print("*" * 100)


############################# classmethod and staticmethod ##################################

class Test2(object):
    cls_nam = "this is a class name"

    def __init__(self):
        self.instance_var = 123

    @classmethod
    def cls_method(cls):
        print(cls.cls_nam)

    @staticmethod
    def static_method():
        print("this is a static method")

    def instance_method(self):
        print(self.cls_nam)


## call class method directly
Test2.cls_method()

### 实例化
t = Test2()
t.cls_method()
t2 = Test2()
t2.cls_method()

t2.instance_method()

## 直接调用静态方法，直接当成函数调用，其并不知道类属性和实例属性
Test2.static_method()
t2.static_method()


# classmethod vs staticmethod
#
# Like a static method, a class method doesn’t need an object to be instantiated.
#
# A class method differs from a static method in that
# !a static method doesn’t know about the class itself.
# ! In a classmethod, the parameter is always the class itself.
#
# a static method ! knows nothing about the class or instance. You can just as well use a function call.
#
# a class method gets the class when the method is called. ! It knows abouts the classes attributes and methods.


# Q1:怎么限制实例不能修改访问类变量呢
# a1: _slots_

class Test3(object):
    cls_var = "this is cls variable"

    __slots__ = ["in_Var1", "in_Var2"]

    def __init__(self):
        self.in_Var1 = 123
        self.in_Var2 = 321


TT = Test3()
print(TT.cls_var)
TT.in_Var1 = 22  # 可以改变
TT.add = 55 # error 不在__slots__ 不能创建
TT.cls_var = 22  # error ! 只读

print(Test3.cls_var)  # OK
