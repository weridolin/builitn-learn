# -*- encoding: utf-8 -*-

#  重命名类型
### example 1
from typing import List

Vector = List[float]

def scale(scaler:float,vector:Vector)->Vector:
    return [scaler*num for num in vector]

new_vector = scale(2.0,[1.0,-4.2,5.4])
print(new_vector)
### example 2
from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

# 更优雅的写法
def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
        message: str,
        servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:

    pass


# NewType
### example 1
from typing import NewType
UserID = NewType("UserID",int) # INT的子类
def get_user_name(user_id: UserID):
    print(user_id)
    return

# typechecks
user_a = get_user_name(UserID(42351))
# does not typecheck; an int is not a UserId
user_b = get_user_name(-1)

# Callable
### example 1

from typing import Callable
# 一个可调用的函数，一般用于参数中有一个函数

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None],
                notArg:Callable[..., int]) -> None:
    pass
# 参数1 on_success--->一个函数，参数为1个，int类型，返回None
# 参数2 on_error-->可调用函数: Callable[[int, Exception], None] 参数为2个：int类型和Exception类习惯,返回None
def argFunction(arg1:str,arg2:int)->None:
    print(arg1,arg2)

def argFunction2(arg1:str,arg2:str)->None:
    print(arg1,arg2)

def callableFunction(argFunction:Callable[[str,int],None],arg1,arg2):
    return argFunction(arg1,arg2)

callableFunction(argFunction,"2",1)
callableFunction(argFunction2,"2",1) # 类型不匹配,但是仍可以输出


# TypeVar
from typing import TypeVar
T = TypeVar('T')            # <-- 'T' can be any type
A = TypeVar('A', str, int)  # <-- 'A' will be either str or int

def argT(arg:T):
    print(arg)

def argA(arg:A):
    print(arg)

# argT(2)
# argT("Ss")
# argT([2,"S",1.0])
#
# argA(2)
# argA("Ss")
# argA([1,3]) #可以运行，但类型检测会出错

# Generic
### 泛型
from typing import TypeVar,Generic,List
T2 = TypeVar("T2")
class Stack(Generic[T2]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push('x')
print(stack.items)
