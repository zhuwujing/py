# 读取文件,得到一个文件流，文件不存在会报错
f = open('1.txt')
buf = f.read()
print(buf)
f.close()

# 写文件  文件不存在，会创建文件；文件存在，会覆盖清空源文件内容
f = open('1.txt', 'w', encoding='utf-8')
f.write('hello world')
f.close()

# 追加文件
f = open('1.txt', 'a')
f.write("是谁？")
f.close()

