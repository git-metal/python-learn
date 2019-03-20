import socket
import sys

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]

# 传入链接参数
server_address = ('localhost', 9999)

# Create a TCP/IP socket
# 使用列表生成式，生成多个请求。
# Winuds使用select支持并发并不多 这里测试40个并发
# Linux默认使用epoll可支持上万并发可修改10000
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          for i in range(40)]

print('connecting to %s port %s' % server_address)

# 循环socks连续链接4次
for s in socks:

    s.connect(server_address)

# 循环发送数据
for message in messages:

    # Send messages on both sockets
    # 每个客户端依次发送数据
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)

    # Read responses on both sockets
    # 服务端收数据
    for s in socks:
        data = s.recv(1024)

        # getsockname()服务端返回
        print( '%s: received "%s"' % (s.getsockname(), data) )

        # 没有数据打印客户端要关闭了
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname() )