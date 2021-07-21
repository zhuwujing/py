print('Hello World!')
name = 'gaga'


def change_global():
    global name
    name = 'wei'
    print(name)
    pass


def add(a, b):
    return a+b


def say_hello():
    """
    我是一个函数文档说明
    :return:
    """
    print('i say Hello ')


def test():
    pass


print(f"hello_world__name__ = {__name__}")
change_global()
print(name)


