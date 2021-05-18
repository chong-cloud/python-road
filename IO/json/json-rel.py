import json
"""
变量从内存中变成可存储或传输的过程称之为"序列化"
变量内容从序列化的对象重新读到内存里称之为"反序列化"

# loads： 是将string转换为dict
# dumps： 是将dict转换为string
# load： 是将里json格式字符串转化为dict，读取文件
# dump： 是将dict类型转换为json格式字符串，存入文件
"""
def json_dumps_loads():
    # data = {'first_name': 'Wonderful', 'last_name': 'Spam', 'Adress': '北京路'}
    # 使用下面这行数据，则json_dict为list类型
    data = [{'first_name': 'Wonderful', 'last_name': 'Spam', 'Adress': '北京路'}]
    json_str = json.dumps(data, ensure_ascii=False)  # 字典转成json类型(字符串),ensure_ascii默认为True，要输出中文需要设置为false
    print('原始数据：', data)
    print('字典转json:', json_str, type(json_str))
    json_dict = json.loads(json_str)  # 　json字符串转为python对象
    print('json转字典', json_dict, type(json_dict))


def json_write():
    data = {'first_name': 'Wonderful', 'last_name': 'Spam', 'Adress': '北京路'}
    file = open('infor.json', 'w', encoding='utf8')
    json.dump(data, file, ensure_ascii=False) # 写入json数据
    file.close()


def json_read():
    file = open('infor.json', 'r', encoding='utf8')
    data = json.load(file)  # 读出json数据
    print(data, type(data))
    file.close()


json_dumps_loads()
json_write()
json_read()
