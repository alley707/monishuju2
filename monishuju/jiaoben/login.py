# _*_ coding:utf-8 _*_

import csv
import os
import time
import diaoyongjar
from socket import *

class login:
    def get(self, nob, noc):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/boyunshikong/boxbox/login.csv"
        fCase = open(file_path, "r", encoding="gbk")
        datas = csv.reader(fCase)
        datas1 = []
        o = 0
        for line in datas:
            datas1.append(line)
        for nob1 in range(1, nob):
            t = datas1[nob1]
            o += 1
            # print(t)
            print('发送第%d条' % o)

            #识别位
            sbw = t[0]
            print(sbw)

            #命令单元
            mldy = t[1]
            mldy1 = mldy.zfill(2)
            print(mldy1)

            #车辆识别号
            clsbh = t[2]
            print(clsbh)

            #软件版本号
            rjbbh = t[3]
            rjbbh1 = rjbbh.zfill(2)
            print(rjbbh1)

            #数据加密方式
            jm = t[4]
            jm1 = jm.zfill(2)
            print(jm1)

            #数据单元长度
            sjdycd = t[5]
            print(sjdycd)

            #数据采集时间
            ti = time.strftime("%Y%m%d%H%M%S")
            ti2 = str(ti)
            ti3 = 2 * '' + ti2[2:]
            ti4 = (hex(int(ti3[0:2]))[2:4]).zfill(2)
            ti5 = (hex(int(ti3[2:4]))[2:4]).zfill(2)
            ti6 = (hex(int(ti3[4:6]))[2:4]).zfill(2)
            ti7 = (hex(int(ti3[6:8]))[2:4]).zfill(2)
            ti8 = (hex(int(ti3[8:10]))[2:4]).zfill(2)
            ti9 = (hex(int(ti3[10:12]))[2:4]).zfill(2)
            ti10 = ti4 + ti5 + ti6 + ti7 + ti8 + ti9
            print(ti10)
            #流水号
            llh = t[7]
            print(llh)

            #设备序列号
            sbxlh = t[8]
            print(sbxlh)

            w = sbw+mldy1+clsbh+rjbbh1+jm1+sjdycd+ti10+llh+sbxlh
            print(w)

            #组合校验
            data = w
            a = diaoyongjar.get_xor(data)
            b = diaoyongjar.get_bcc(a).zfill(2)
            # print(b)
            s = w + b
            # print(s)

            #发送
            t = a + ' ' + b
            print(t)
            # s.send(bytes().fromhex(sj))
            s = socket(AF_INET, SOCK_STREAM)
            # s.connect(('120.77.17.210',8010)) #测试
            # s.connect(('120.77.133.46', 8010))  # 开发
            s.connect(('47.113.58.88',8010)) #正式
            # s.connect(('106.112.219.162', 8010))  # 泊头
            # s.connect(('47.106.76.236', 8010))  # docker
            s.send(bytes().fromhex(t))
            print('\n' * 1)
            time.sleep(1)
            s.close()


if __name__ == '__main__':
    ll = login()
    ll.get(2,1)



