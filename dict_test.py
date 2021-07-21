# 空字典
my_dict = {}
print(type(my_dict), my_dict)

my_dict1 = dict()
print(type(my_dict1), my_dict1)

# 定义字典
my_dict2 = {'name': '孙悟空', 'age': 18, 'address': '湖北', 1: [1, 2, 3]}
print(my_dict2)

print(my_dict2['name'])
print(my_dict2[1][1])
# print(my_dict2['hah'])  报错 KeyError: 'hah'
print(my_dict2.get('name'))
print(my_dict2.get('name1', 'default'))
print(len(my_dict2))
