import socket

# 创建 socket 对象
# family(协议族):AF_INET(IPv4) AF_INET6(IPv6) type(套接字类型) SOCK_STREAM(TCP协议-流式socket) SOCK_DGRAM(UDP协议-数据报式socket)
# family参数代表地址家族，可为AF_INET或AF_UNIX。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。
# type参数代表套接字类型，可为SOCK_STREAM(流套接字，就是TCP套接字)和SOCK_DGRAM(数据报套接字，就是UDP套接字)。
# 默认为family=AF_INET  type=SOCK_STREM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 9999

# ip地址相关
hostk = socket.gethostbyname(socket.gethostname())
print("ip地址：", hostk)
addrs = socket.getaddrinfo(socket.gethostname(), None)
for item in addrs:
    print(item)
# 仅获取当前IPV4地址
for item in addrs:
    if ':' not in item[4][0]:
        print('当前主机IPV4地址为:' + item[4][0])


# 绑定端口号,参数是元组(主机， 端口号)，若出现问题，例如端口占用，报错：socket.error
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接，阻塞函数，一致等待客户端访问
    # accept方法返回一个含有两个元素的元组(connection,address)。
    # 第一个元素connection是所连接的客户端的socket对象（实际上是该对象的内存地址），服务器必须通过它与客户端通信；
    # 第二个元素 address是客户的Internet地址。
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问！' + "\r\n"
    # 发送的数据为2进制的
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

serversocket.close()