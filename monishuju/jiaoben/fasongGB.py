# -*- coding:utf-8 -*-
from shujuzuhejiaoyanGB import ZuHeJiaoYan
from shujuzuhejiaoyanGB import MyFTP
from configobj import ConfigObj
import time
import threading
import binascii
import socket
import csv
import os



class fasongGB(object):
    def __init__(self):
        conf_ini = os.path.dirname(os.path.dirname(__file__)) + "\\conf\\config.ini"
        config = ConfigObj(conf_ini, encoding='UTF8')
        hj = config['HJ']['hj']
        wg = config[hj]['shikong_wg']
        wg_port = config[hj]['shikong_wg_port']
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP连接
        self.s.settimeout(5)  # 设置连接超时时间
        self.s.connect((wg, int(wg_port)))  # 连接网关
        self.JY = ZuHeJiaoYan()  # 组合校验

    def piliang(self):
        try:
            s = self.s
            path = os.path.dirname(os.path.dirname(__file__))
            file_path = path + "/excelFile/boyunshikong/youlian.csv"
            fCase = open(file_path, "r", encoding="gbk")
            datas = csv.reader(fCase)
            n = 0
            m = 0
            x = 0
            for arr in datas:
                if n == 0:
                    n += 1
                    continue
                sj = self.JY.pinjiejiaoyan(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
                s.send(bytes().fromhex(sj))
                try:
                    print(sj)
                    print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
                except:
                    x += 1
                m += 1
                print(m)
            print("一共发送%d条数据，其中%d条发送失败！" % (m, x))
        except Exception as e:
            print("批量上线车辆失败！原因：%s" % e)

    def dantiao(self, shebeihao, baojing, status, weidu, jingdu, gaocheng, sudu, fangxiang, fjxx):
        s = self.s
        sj = self.JY.pinjiejiaoyan(shebeihao, baojing, status, weidu, jingdu, gaocheng, sudu, fangxiang, fjxx)
        s.send(bytes().fromhex(sj))
        try:
            print(sj)
            print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
        except:
            print("发送失败！")


    def guiji(self, shebeihao):
        s = self.s
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/boyunshikong/youlian.csv"
        fCase = open(file_path, "r", encoding="gbk")
        datas = csv.reader(fCase)
        n = 0
        m = 0
        x = 0
        for arr in datas:
            if n == 0:
                n += 1
                continue
            sj = self.JY.pinjiejiaoyan(shebeihao, arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8])
            time.sleep(2)
            s.send(bytes().fromhex(sj))
            try:
                print(sj)
                print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
            except:
                x += 1
            m += 1
            print(m)
        print("一共发送%d条数据，其中%d条发送失败！" % (m, x))
        fCase.close()

    def zidingyishuju(self, data):
        s = self.s
        data = data.replace(" ", "")
        sj = self.JY.jiaoyanGB(data)
        s.send(bytes().fromhex(sj))
        try:
            print(sj)
            print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
        except:
            print("发送失败！")

    def bsj_adas_data(self, shebeihao, ccqlx, ycjsxwlx, wzxxhb, alarm_files):
        s = self.s
        with MyFTP() as FtP:
            lis = []
            path = os.path.dirname(os.path.dirname(__file__))
            for alarm_file in alarm_files:
                file_path = path + "/multimedia/%s" % alarm_file
                list_info = FtP.ftp_upload(file_path, "/adas/image/%s" % alarm_file)  # 上传文件
                lis.append(list_info)
            sj = self.JY.pinjie_adas_data(shebeihao, ccqlx, ycjsxwlx, wzxxhb, "/adas/image/", lis)
            s.send(bytes().fromhex(sj))
            print(sj)

    def piliang_sx(self):
        s = self.s
        BY = self.JY
        m = 0
        n = 0
        while True:
            for wd in [22.073636, 22.075636, 22.077636]:
                n += 1
                zdbh = 13655550000
                for _ in range(50000):
                    zdbh += 1
                    m += 1
                    print(str(m) + threading.current_thread().name)
                    wd += 0.0002
                    sj = BY.pinjiejiaoyan(str(zdbh), "超速报警", "ACC开，已定位", str(wd), "114.329832", "10", "90", "360", "")
                    s.send(bytes().fromhex(sj))
                    # s.recv(1024)
                    time.sleep(5)
                print(n)

    def disconnect(self):
        self.s.send(b'exit')
        self.s.close()

    def jiashiyuan_data(self, arr):
        s = self.s
        sj = self.JY.pinjie_0702_data(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6])
        s.send(bytes().fromhex(sj))
        try:
            print(sj)
            print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())
        except:
            print("发送失败！")


if __name__ == "__main__":
    LL = fasongGB()
    # taiya = "胎压：[['左轮', '1', '75℃', '2Bar', '3Bar', '50%', '2.5Bar', '60摄氏度']," \
    #         "['左轮', '3', '75℃', '2Bar', '3Bar', '50%', '4Bar', '60摄氏度']," \
    #         "['右轮', '2', '75℃', '2Bar', '3Bar', '50%', '1Bar', '60摄氏度']," \
    #         "['右轮', '4', '75℃', '2Bar', '3Bar', '50%', '2.5Bar', '90摄氏度']]"
    # youliang = "油量：70%"
    # shudu = "速度：111"
    # "36.073636", "114.329932"
    # dq = "登签：登签 (7654321)"

    # fj = dq
    # LL.dantiao("13533443344", "", "ACC开，已定位，满载", "36.073636", "114.359932", "10", "60", "0", fj)
    # LL.piliang()
    LL.guiji("18888888888")
    # while True:
    #     time.sleep(30)
    #     LL.guiji("13433003300")



#
# while True:
#     time.sleep(10)
#     gg = fasongGB()
#     gg.guiji("13000013311")







    # mdvr = "MDVR状态：{'网络状态': {'网络制式': '3G', '信号强度': '差'}}"
    # fj = ""
    # LL.dantiao("13577117711", "", "ACC开，已定位，半载", "36.073636", "114.359932", "10", "50", "0", fj)

    #  adas 报警
    # ycbj = ["吸烟", "疲劳"]
    # wz = ["", "ACC开，已定位", "36.073636", "114.329832", "10", "90", "0"]
    # files = ["pilaojiashi.mp4", "pilaojiashi1.png", "pilaojiashi2.png", "pilaojiashi3.png"]
    # LL.bsj_adas_data("13577117711", "主存储器", ycbj, wz, files)

    # LL.piliang_sx()
    # # 创建数组存放线程
    # threads = []
    # # 创建线程
    # for i in range(1, 11):
    #     # 针对函数创建线程
    #     t = threading.Thread(name="线程%s" % str(i), target=LL.piliang_sx)
    #     # 把创建的线程加入线程组
    #     threads.append(t)
    # # 启动线程
    # for thread in threads:
    #     thread.setDaemon(True)
    #     thread.start()
    #     sleep(30)

    # 驾驶员登签数据
    # LL.jiashiyuan_data(["13577117711", "插入", "读卡成功", "楚风", "7654321", "博实结科技", "20230115"])
    # LL.disconnect()



