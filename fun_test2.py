a = 10
b = a

print(id(a))
print(id(b))

b = 1
print(f"a={a}")
print(f"b={b}")

my_tuple = (1, 2, 3)
# my_tuple[2] = 10  TypeError: 'tuple' object does not support item assignment
print(my_tuple[1])
