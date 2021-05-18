# CSV文件读取的两种方式
import csv

# CSV文件写入的两种方式
# 列表写入
# 设置记录标题(列表)和记录值(一个嵌套元组集或列表集的列表)


def csv_writer():
    headers = ['id', 'name', 'province']
    values = [
        ('001', 'ShenZhen', 'GuangDong'),
        ('002', 'WuHan', 'HuBei'),
        ('003', 'ChengDu', 'SiChuan')
    ]
    # 使用open函数时设置参数encoding以防止乱码
    with open('citylist.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)  # 获取文件
        writer.writerow(headers)  # 写入一行记录
        writer.writerows(values)  # 写入多行记录，传入的参数为列表结构

    # 字典写入
    # 设置记录标题(列表)和记录值(一个嵌套字典集的列表)
    headers = ['id', 'name', 'province']
    values = [
        {'id': '001', 'name': 'ShenZhen', 'province': 'GuangDong'},
        {'id': '002', 'name': 'WuHan', 'province': 'HuBei'},
        {'id': '003', 'name': 'ChengDu', 'province': 'SiChuan'}
    ]
    with open('citydict.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)  # 获取文件，注意参数还需传递记录标题以映射，注意此时并不会真正写入标题
        writer.writeheader()  # 写入记录标题
        writer.writerows(values)  # 写入多行记录


def csv_reader():
    # 列表读取
    with open('citylist.csv', 'r') as fp:
        reader = csv.reader(fp)  # 返回读取迭代器
        titles = next(reader)  # 提取出文件记录标题
        print(type(titles))  # <class 'list'>
        print(titles)  # ['id', 'name', 'city']
        for x in reader:  # 遍历向下迭代
            print(x)  # ['001', 'Mike', 'Beijing']...
            id = x[0]
            name = x[1]
            city = x[2]
            print({'id': id, 'name': name, 'province': city})  # {'id': '001', 'name': 'Mike', 'province': 'Beijing'}

    # 字典读取
    with open('citylist.csv', 'r') as fp:
        reader = csv.DictReader(fp)  # 迭代器，但不包含标题数据(第0行)
        for x in reader:
            print(type(x))  # <class 'collections.OrderedDict'>
            print(x)  # OrderedDict([('id', '001'), ('name', 'Mike'), ('city', 'Beijing')])...
            id = x['id']
            name = x['name']
            city = x['province']
            print({'id': id, 'name': name, 'province': city})  # {'id': '001', 'name': 'Mike', 'province': 'Beijing'}


csv_writer()
csv_reader()
