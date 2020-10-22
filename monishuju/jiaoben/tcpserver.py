# _*_ coding:utf-8 _*_

# coding=utf-8
import socket

BUF_SIZE = 1024
host = 'localhost'
port = 8091

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, address = server.accept()


def data(a):
    while True:
        data = client.recv(BUF_SIZE).decode('utf-8')
        if data == a :
            data1 = 'succeed'
            client.send(data1.encode())
            break
        else:
            data2 = 'error'
            client.send(data2.encode())
            print(data2)
        # client.close() 长连接

if __name__ == '__main__':
    a = '1'
    b = '2'
    c = '3'

    s = data(a)
    p = data(b)
    d = data(c)
    l = data(a)









