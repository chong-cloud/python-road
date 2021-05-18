# mode参数：默认为r
# 只读：r
# 只写：w-文件存在则覆盖(若文件存在的内容会被删除)，不存在就创建文件；a-文件存在则新增内容跟在已存在内容后，文件指针在内容之后，不存在就创建文件，
# 可读可写：w+，a+，r+，
# +-打开一个文件更新，可读可写；
# b-二进制模式；（以上模式可组合）

# buffering为0：无缓存；为1：有缓存；大于1：寄存区的缓冲大小；负值：系统默认寄存区的缓冲大小
file = open("aa.txt", "r+", buffering=1, encoding="utf-8")

data = file.read().splitlines()
print(data)

file.seek(0)
print(file.read(2))
print(file.readline())   # 读完后，文件指针已经改变，readlines只能读取到一条数据
print(file.readable())
for line in file.readlines():
    print(line)

# 改变文件指针位置，再读
file.seek(0)
print(file.readable())
for line in file.readlines():
    print(line)

file.write("\n你应该在最后出现")
string = ["\nfirst", " and ", "second"]
file.writelines(string)

file.close()

# # 查看文件指针
# fp.tell()
# # 刷新缓冲区和fp.close()类似
# fp.flush()

