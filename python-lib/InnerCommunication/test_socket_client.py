#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 9999
CLIENT_PORT = 9990

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, CLIENT_PORT)) #bind client port
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    s.sendall("hello world!".encode('ascii'))
    data = s.recv(1024)
    print('Received', repr(data.decode('utf8')))
    while True:
        msg = input()
        s.sendall(msg.encode('ascii'))
        data = s.recv(1024)
        print('Received:%s' % repr(data.decode('utf8')))
