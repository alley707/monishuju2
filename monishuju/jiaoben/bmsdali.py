# _*_ coding:utf-8 _*_

# coding:utf-8
import csv
import os
import time
import diaoyongjar
import bbjiaoyan
from socket import *
import binascii

class out:
    def get(self, nob, noc):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/boyunshikong/boxbox/bmsdali.csv"
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

            tou = t[0]
            # print(tou)

            id = t[1]
            # print(id)

            cd = t[2]
            # print(cd)

            sbh = t[3]
            # print(sbh)

            lsh = t[4]
            # print(lsh)

            ti = time.strftime("%Y%m%d%H%M%S")
            ti2 = str(ti)[2:]
            # print(ti2)

            bmsbanlx = t[6]
            # print(bmsbanlx)

            bmssjcd = t[7]
            # print(bmssjcd)

            zdy = t[8]
            # print(zdy)

            zdl = t[9]
            # print(zdl)

            soc = t[10]
            # print(soc)

            soh = t[11]
            # print(soh)

            zgdtdy = t[12]
            # print(zgdtdy)

            zgdtdyxh = t[13]
            # print(zgdtdyxh)

            zddtdy = t[14]
            # print(zddtdy)

            zddtdyxh = t[15]
            # print(zddtdyxh)

            zdyc = t[16]
            # print(zdyc)

            zgwd = t[17]
            # print(zgwd)

            zgwdxh = t[18]
            # print(zgwdxh)

            zdwd = t[19]
            # print(zdwd)

            zdwdxh = t[20]
            # print(zdwdxh)

            bjzt1 = t[21]
            # print(bjzt1)

            bjzt2 = t[22]
            # print(bjzt2)

            bhzt1 = t[23]
            # print(bhzt1)

            bhzt2 = t[24]
            # print(bhzt2)

            zgzt = t[25]
            # print(zgzt)

            xtzt = t[26]
            # print(xtzt)

            dtdyggbhz = t[27]
            # print(dtdyggbhz)

            dtdygghhz = t[28]
            # print(dtdygghhz)

            dtdyggbjz = t[29]
            # print(dtdyggbjz)

            dtdyggbjyc = t[30]
            # print(dtdyggbjyc)

            dtdyggbhhhyc = t[31]
            # print(dtdyggbhhhyc)

            dtdyggbjyc = t[32]
            # print(dtdyggbjyc)

            dtdybhnsbz = t[33]
            # print(dtdybhnsbz)

            wdcgqgs = t[34]
            # print(wdcgqgs)

            wd0 = t[35]
            # print(wd0)

            wd1 = t[36]
            # print(wd1)

            wd2 = t[37]
            # print(wd2)

            wd3 = t[38]
            # print(wd3)

            wd4 = t[39]
            # print(wd4)

            wd5 = t[40]
            # print(wd5)

            dtdcgs = t[41]
            # print(dtdcgs)

            jhzt = t[42]
            # print(jhzt)

            d1dy = t[43]
            # print(d1dy)

            d2dy = t[44]
            # print(d2dy)

            d3dy = t[45]
            # print(d3dy)

            d4dy = t[46]
            # print(d4dy)

            d5dy = t[47]
            # print(d5dy)

            d6dy = t[48]
            # print(d6dy)

            d7dy = t[49]
            # print(d7dy)

            wei = t[50]
            # print(wei)


            w = tou+id+cd+sbh+lsh+ti2+bmsbanlx+bmssjcd+zdy+zdl+soc+soh+zgdtdy+zgdtdyxh+zddtdy+zddtdyxh+zdyc+zgwd+zgwdxh+zdwd+zdwdxh+bjzt1+bjzt2+zgzt+xtzt+dtdyggbhz+dtdygghhz+dtdyggbhz+dtdygghhz+dtdyggbjz+dtdyggbjyc+dtdyggbhhhyc+dtdyggbjyc+dtdybhnsbz+wdcgqgs+wd0+wd1+wd2+wd3+wd4+wd5+dtdcgs+jhzt+d1dy+d2dy+d3dy+d4dy+d5dy+d6dy+d7dy+wei
            # w = tou+id+cd+sbh+lsh+ti2+bmsbanlx+bmssjcd+zdy+zdl+soc+soh+zgdtdy+zgdtdyxh+zdyc+zgwd+zgwdxh+zdwd+zdwdxh+bjzt1+bjzt2+bhzt1+bhzt2+zgzt+xtzt+dtdyggbhz+dtdygghhz+dtdyggbjz+dtdyggbjyc+dtdyggbhhhyc+dtdyggbjyc+dtdybhnsbz+wdcgqgs+wd0+wd1+wd2+wd3+wd4+wd5+dtdcgs+jhzt+d1dy+d2dy+d3dy+d4dy+d5dy+d6dy+d7dy+wei

            # print(w)
            # print('\n' * 1)

            data = w
            a = diaoyongjar.get_xor(data)
            # print(a)
            # print('\n' * 1)

            a1 = bbjiaoyan.jiaoyanGB(a)
            # print(a1)
            # print('\n' * 1)

            a2 = diaoyongjar.get_xor(a1)
            print(a2)

            s = socket(AF_INET, SOCK_STREAM)
            # s.connect(('192.168.100.226', 7004))
            s.connect(('112.74.74.215', 7004))
            s.send(bytes().fromhex(a2))
            print('\n' * 1)
            # time.sleep(3)
            # s.close()
            # mag = s.recv(1024)
            # print(mag)
            # print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())



if __name__ == '__main__':
    # ll = out()
    # ll.get(2, 1)

    while True:
        time.sleep(1)
        oo = out()
        oo.get(2,1)



