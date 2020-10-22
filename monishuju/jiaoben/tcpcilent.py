# _*_ coding:utf-8 _*_
import socket
import time

def sscc() :

    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client_socket.connect(("116.62.230.113", 9200))

    send_connect = "7878252612070C0E1F10C502781E640C445CA00014490801CC00262C000EBA4C00030000006BBE850D0A"

    tcp_client_socket.send(bytes().fromhex(send_connect))

    recv_data = tcp_client_socket.recv(1024)
    recv_content = recv_data.decode("gbk")
    print("接受服务端的数据为：", recv_content)

    # tcp_client_socket.close()

if __name__ == '__main__':
    while True:
        pp = sscc()
        time.sleep(1)


