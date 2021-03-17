

def method1():
    print("method 1")

def method2():
    print("method 2")


class Test:
    methods=[
    "method1",
    "method2"
    ]

    def __getattr__(self, item):
        print(item,type(item))
        if item in self.methods:
            return eval(item())


if __name__ == '__main__':
    T = Test()


    