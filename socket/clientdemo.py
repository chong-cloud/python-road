import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 设置端口号
port = 9999
# 连接服务，指定主机和端口
s.connect((host, port))
# 同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
# s.connect_ex((host, port))
# 接收小于 1024 字节的数据,是阻塞函数,会一直等待
msg = s.recv(1024)
print(msg.decode('utf-8'))
print(type(msg.decode('utf-8')))

# 与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
# msg = s.recvfrom(1024)

print(type(msg))
s.close()

# print(msg[0].decode('utf-8'))
# print(msg[1])
# print(type(msg[0].decode('utf-8')))