def print_list(my_list0):
    for item0 in my_list0:
        print(item0)


# 空列表
my_list = [1, 2, 3, 4, 9, 8, 3]
my_list1 = list()
print(type(my_list), my_list)
print(type(my_list1), my_list1)

my_list2 = [1, "hello", True, False, [1, 2, 3]]
print(len(my_list2))
print(my_list2[4])
print(my_list2[::-1])
print(my_list2[1:2])
print(my_list2)

# 遍历
for item in my_list2:
    print(item)

j = 0
while j < len(my_list2):
    print(my_list2[j])
    j += 1

a = 5
b = 5
print(id(a))
print(id(b))

print("*" * 50)
my_list2.append("qwe")
print_list(my_list2)
print(my_list2)

my_list2.insert(0, "add")
print(my_list2)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

print(my_list.count(3))

my_list2.remove("add")
print(my_list2)

print(my_list2.pop())
print(my_list2)

del my_list2[1]
print(my_list2)






