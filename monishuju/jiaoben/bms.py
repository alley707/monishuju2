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


            sbh = t[0]
            print(sbh)

            shebeihao = t[1]
            print(shebeihao)

            sbh1 = t[2]
            print(sbh1)

            ti = time.strftime("%Y%m%d%H%M%S")
            ti2 = str(ti)[2:]
            print(ti2)

            zl = t[4]
            print(zl)

            cd = t[5]
            print(cd)

            jqbm = t[6]
            print(jqbm)

            ccrq = t[7]
            print(ccrq)

            dcdz = t[8]
            print(dcdz)

            zdcgs = t[9]
            print(zdcgs)

            dczgs = t[10]
            print(dczgs)

            mzdgs = t[11]
            mzdgs1 = mzdgs*16
            print(mzdgs1)

            dcwdcgqgs = t[12]
            print(dcwdcgqgs)

            mgdccgqwd = t[13]
            mgdccgqwd1 = mgdccgqwd*4
            print(mgdccgqwd1)

            glbwd = t[14]
            print(glbwd)

            jhbwd = t[15]
            print(jhbwd)

            dlsj = t[16]
            print(dlsj)

            dlzdy = t[17]
            print(dlzdy)

            dcsyrl = t[18]
            print(dcsyrl)

            dcxhcs = t[19]
            print(dcxhcs)

            bmsjz = t[20]
            print(bmsjz)

            jcqdz7 = t[21]
            print(jcqdz7)

            jcqdz8 = t[22]
            print(jcqdz8)

            zfdl = t[23]
            print(zfdl)

            cdbhdy = t[24]
            print(cdbhdy)

            fdbhdy = t[25]
            print(fdbhdy)

            cdsxbhdy = t[26]
            print(cdsxbhdy)

            fdsxbhdy = t[27]
            print(fdsxbhdy)

            cdhfdy = t[28]
            print(cdhfdy)

            jhqkdy = t[29]
            print(jhqkdy)

            fdglbh = t[30]
            print(fdglbh)

            fdfzbh = t[31]
            print(fdfzbh)

            fdglys = t[32]
            print(fdglys)

            fdfzbh = t[33]
            print(fdfzbh)

            cddlbh = t[34]
            print(cddlbh)

            jhdlbfb = t[35]
            print(jhdlbfb)

            jhjm = t[36]
            print(jhjm)

            glbwdbh = t[37]
            print(glbwdbh)

            glbwdhhz = t[38]
            print(glbwdhhz)

            jhwdbhz = t[39]
            print(jhwdbhz)

            jhwdhhz = t[40]
            print(jhwdhhz)

            dcwdbhz = t[41]
            print(dcwdbhz)

            dcwdhhz = t[42]
            print(dcwdhhz)

            rldbj = t[43]
            print(rldbj)

            dcrlsz = t[44]
            print(dcrlsz)

            jhkg = t[45]
            print(jhkg)

            cdkg = t[46]
            print(cdkg)

            fdkg = t[47]
            print(fdkg)

            zycdqkg = t[48]
            print(zycdqkg)

            dwbhz = t[49]
            print(dwbhz)

            dwhhz = t[50]
            print(dwhhz)

            jyw = t[51]
            print(jyw)
            print('\n' * 1)


            w = sbh+shebeihao+sbh1+ti2+zl+cd+jqbm+ccrq+dcdz+zdcgs+dczgs+mzdgs1+dcwdcgqgs+mgdccgqwd1+glbwd+jhbwd+dlsj+dlzdy+dcsyrl+dcxhcs+bmsjz+jcqdz7+jcqdz8+zfdl+cdbhdy+fdbhdy+cdsxbhdy+fdsxbhdy+cdhfdy+jhqkdy+fdglbh+fdfzbh+fdglys+fdfzbh+cddlbh+jhdlbfb+jhjm+glbwdbh+glbwdhhz+jhwdbhz+jhwdhhz+dcwdbhz+dcwdhhz+rldbj+dcrlsz+jhkg+cdkg+fdkg+zycdqkg+dwbhz+dwhhz+jyw
            print(w)
            print('\n' * 1)

            data = w
            a = diaoyongjar.get_xor(data)
            print(a)
            print('\n' * 1)

            a1 = bbjiaoyan.jiaoyanGB(a)
            print(a1)
            print('\n' * 1)

            a2 = diaoyongjar.get_xor(a1)
            print(a2)

            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('112.74.74.215',7004))
            s.send(bytes().fromhex(a2))
            print('\n' * 1)
            time.sleep(1)
            # s.close()
            # mag = s.recv(1024)
            # print(mag)
            # print(str(binascii.b2a_hex(s.recv(1024)))[2:-1].upper())


if __name__ == '__main__':
    ll = out()
    ll.get(2,1)


