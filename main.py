import hello_world


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    hello_world.say_hello()
    result = hello_world.add(1, 3)
    print(result)


if __name__ == '__main__':
    print_hi('PyCharm')

print(f"main__name__ = {__name__}")
help(hello_world.say_hello)


