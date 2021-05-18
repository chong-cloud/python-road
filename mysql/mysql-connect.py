# python3主用，使用DBUtils进行多线程的操控
import pymysql
db = pymysql.connect("localhost", "root", "111111", "apsaras5", charset='utf8')
cursor = db.cursor()


"""
所有的fetch**()取了数据之后，移动指针就往后移，始终保持指向下一条待取数据
rowcount是指当前execute影响的数量，rownumber则是指数据库中数据的总量

cursor（执行所有操作的主体）中其它方法：
callproc(self, procname, args) 用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
execute(self, query, args) 执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
executemany(self, query, args) 执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
nextset(self) 移动到下一个结果集
"""

# 查数据
cursor.execute("select * from cruddemo")
# 接收一条返回结果
data = cursor.fetchone()
print("count", cursor.rowcount)
# 移动指针到某一行; 如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条.
cursor.scroll(2, mode='relative')
data4 = cursor.fetchone()
# 接收size条返回结果行，size超过总体数量则接收全部结果
data3 = cursor.fetchmany(size=5)
# 接收全部的返回结果行
data2 = cursor.fetchall()
# 接收size条返回结果行，size超过总体数量则接收全部结果

print("Number", cursor.rownumber)


print(data)
# 返回的类型是元素类型
print(type(data))
print(data[1])
print("全部接收")
print(data2)
print("只接收5条")
print(data3)
print("当前指向的结果位置")
print(data4)
db.close()


# # 增、删、改数据
# insertss = "insert INTO cruddemo VALUES (18, '11111111111', '2020-12-28 11:26:32', " \
#            "20201223093759338, NULL, 6, NULL, NULL, 1, '新增', 123, '1', '168', NULL)"
#
# inserts = "insert INTO cruddemo VALUES (19, '11111111111', '2020-12-28 11:26:32', " \
#            "20201223093759338, NULL, 6, NULL, NULL, 1, %s, 123, '1', '168', NULL)"
#
# updatess = "UPDATE cruddemo set COSTNAME = '林更新' WHERE id = 19"
#
# deletess = "delete from cruddemo where id = 18"
#
# try:
#     # 增数据
#     with db.cursor() as cursor:
#         print("添加数据")
#         cursor.execute(insertss)
#         # 或者下面的方法
#         cursor.execute(inserts, "测试一下")
#     db.commit()
#
#     # 改数据
#     with db.cursor() as cursor:
#         print("更改数据")
#         cursor.execute(updatess)
#     db.commit()
#
#     # 删除数据
#     with db.cursor() as cursor:
#         print("删除数据")
#         cursor.execute(deletess)
#     # commit和rollback是针对事务，
#     db.commit()
# except :
#     db.rollback()
# finally:
#     db.close()
