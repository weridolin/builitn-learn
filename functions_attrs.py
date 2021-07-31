# -*- encoding: utf-8 -*-
"""

"""


def test_func(var1,*var2,var3="DEFAULT",**var4):
    """ THIS IS DOC"""
    VAR4 = None
    VAR5 = var1
    var6 = 5656


# 打印参数的默认值
print(test_func.__defaults__)
#  << ('DEFAULT',)

# 打印所有的变量
print(test_func.__code__.co_varnames)

### inspect 查看函数相关属性
from inspect import signature
sig = signature(test_func)
for name,param in sig.parameters.items():
    print(name,param.kind,param.default)
    # print(param.kind) # 参数类型
    # print(param.default) # 默认值

# 返回值
print(sig.return_annotation)

