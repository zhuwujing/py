# 定义类
class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(id(self))
        print(f"{self.name}在玩啥")
    pass

    def __str__(self):
        return self.name


dog = Dog("小黑")
dog.play()
print(id(dog))

print(dog)

# dog1 = Dog()
# print(id(dog1))

try:
    a = 1 / 0
except Exception as e:
    print('异常', e)


class Cat():
    pass


class Fish:
    pass

