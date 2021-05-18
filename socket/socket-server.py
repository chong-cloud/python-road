"""
作用：SocketServer简化了网络服务器的编写
socketserver的服务类：
5种类型：BaseServer，TCPServer，UnixStreamServer，UDPServer，UnixDatagramServer。
BaseServer不直接对外服务。
TCPServer针对TCP套接字流
UDPServer针对UDP数据报套接字
UnixStreamServer和UnixDatagramServer针对UNIX域套接字，不常用。

socketserver的请求处理类：
3种类型：BaseRequestHandler，以及它的派生类StreamRequestHandler和DatagramRequestHandler——重写了setup()和finish()方法，handle()留给用户重写

TCPServer是接收到请求后执行handle方法，如果前一个的handle没有结束，那么其他的请求将不会受理，新的客户端也无法加入。
ThreadingTCPServer和ForkingTCPServer则允许前一连接的handle未结束也可受理新的请求和连接新的客户端；
它们的区别在于前者用建立新线程运行handle，后者用新进程运行handle

UDP同理
"""


import socketserver
from time import ctime

# StreamRequestHandler实现TCP/UDP服务器的服务处理器,当只能使用数据流的连接
class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):  # 重写接收响应函数
        print('连接到:', self.client_address)
        data = self.rfile.readline().strip()
        print(data)
        self.wfile.write(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

# 服务端
import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # 创建一个链接,继承于socketserver中的BaseRequestHandler类
        conn = self.request
        # 发送登录提示
        conn.sendall(b"Welcome to login...")
        print("Client connect...")
        while True:
            print("Waitting for recving message...")
            # 接收消息
            message = conn.recv(1024)
            print(message.decode('utf-8'))
            # 收到exit就退出
            if message == "exit":
                break
            # 回复消息
            data = input("Reply message:")
            # 发送消息
            conn.sendall(data.encode('utf-8'))
if __name__ == "__main__":
    # 实例化
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 999, ), MyServer)
    # 调用serve_forever方法
    server.serve_forever()


# 客户端
import socket
sock = socket.socket()
# 连接服务端
sock.connect(('127.0.0.1', 999, ))
login = sock.recv(1024)
print(login.decode('utf-8'))
while True:
    message = input("Please input the message:").strip()
    if message == "exit":
        sock.sendall(b'exit')
        break
    else:
        sock.sendall(message.encode('utf-8'))
        print("Waitting for recving message...")
        data = sock.recv(1024)
        print(data.decode('utf-8'))
sock.close()

