# coding = gbk
from jiaoben.shujuzuheV3 import pinjie
from configobj import ConfigObj
from time import sleep
import binascii
import socket
import csv
import os


class fasongV3(object):
    def __init__(self):
        conf_ini = os.path.dirname(os.path.dirname(__file__)) + "\\conf\\config.ini"
        config = ConfigObj(conf_ini, encoding='UTF8')
        hj = config['HJ']['hj']
        self.wg = config[hj]['ddc_wg']
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP连接
        self.s.settimeout(5)
        self.s.connect((self.wg, 6695))

    def piliang(self):
        s = self.s
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/diandongche/cheliangshuju.csv"
        fCase = open(file_path, "r", encoding="gbk")
        datas = csv.reader(fCase)
        lis = []
        n = 0
        for data in datas:
            if n == 0:
                n += 1
                continue
            lis.append(data)
        fCase.close()
        PJ = pinjie()  # 拼接
        # 发送登录数据
        dlsj = PJ.denglushuju(lis[1][1])
        s.send(bytes().fromhex(dlsj))
        print(dlsj)
        print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
        # 发送位置数据
        m = 0
        x = 0
        for li in lis:
            # DLsj = PJ.denglushuju(li[1])
            # data1 = JY.jiaoyan(DLsj)
            # s.send(bytes().fromhex(data1))
            wzsj = PJ.weizhishuju(li[2], li[3], li[4], li[5], li[6], li[7])
            s.send(bytes().fromhex(wzsj))
            try:
                print(wzsj)
                print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
            except Exception:
                x += 1
            m += 1
            sleep(1)
        print("一共发送%d条数据，其中%d条发送失败！" % (m, x))

    def dantiao(self, li):
        s = self.s
        PJ = pinjie()
        dlsj = PJ.denglushuju(li[0])
        s.send(bytes().fromhex(dlsj))
        print(dlsj)
        print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
        wzsj = PJ.weizhishuju(li[1], li[2], li[3], li[4], li[5], li[6])
        s.send(bytes().fromhex(wzsj))
        print(wzsj)
        print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())


if __name__ == "__main__":
    LL = fasongV3()
    # LL.piliang()  # 15505682703  15505681424
    arr = ["15515686848", "22.642526", "114.035032", "50", "定位", "", ""]  # "863015576768686"
    LL.dantiao(arr)
