

def method1():
    print("method 1")

def method2():
    print("method 2")


class Test():
    methods=[
    "method1",
    "method2"
    ]

    def __init__(self):
        self.x =1

    def __getattr__(self, item):
        # 调用 Test().method1 ,并且method1不存在，即属性不存在时才会进入此方法
        print(item)
        if item in self.methods:
            return eval(item)()


    def __getitem__(self, item):
        # Test()['method1'] 会进入此方法
        if item in self.methods:
            return eval(item)()
        else:
            raise KeyError(f"{item}")


    def __add__(self, other):
        # Test()+2 会进入此方法
        print(f"相加：{other}")
        return


    def __contains__(self, item):
        # k in Test():会调用
        if item in ["test"]:
            return True


    def __missing__(self, key):
        #  __missing__ 方法，在 __getitem__ 碰到找不到的键的时候（继承dict ），Python 就会自动调用它，
        print(f"missing is call by key:{key}")

