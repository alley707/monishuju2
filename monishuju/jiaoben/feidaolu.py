# _*_ coding:utf-8 _*_
import csv
import os
import time
import diaoyongjar
from socket import *

class login:
    def get(self, nob, noc):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/boyunshikong/boxbox/feidaolu.csv"
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
            # print(type(sbw))

            #命令单元
            mldy = t[1]
            mldy1 = mldy.zfill(2)
            print(mldy1)
            # print(type(mldy1))

            #车辆识别号
            clsbh = t[2]
            print(clsbh)
            # print(type(clsbh))

            #软件版本号
            rjbbh = t[3]
            rjbbh1 = rjbbh.zfill(2)
            print(rjbbh1)
            # print(type(rjbbh1))

            #数据加密方式
            jm = t[4]
            jm1 = jm.zfill(2)
            print(jm1)
            # print(type(jm1))

            #数据单元长度
            sjdycd = t[5]
            print(sjdycd)
            # print(type(sjdycd))

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
            # print(type(ti10))

            #数据类型
            llh = t[7]
            llh1 = llh.zfill(2)
            print(llh1)
            # print(type(llh))

            #流水号
            liushuihao = t[8]
            liushuihao1 = liushuihao.zfill(4)
            print(liushuihao1)

            #速度
            sd = t[9]
            sd1 = int(sd)*256
            sd2 = hex(sd1)[2:].zfill(4)
            print('速度',sd2)

            #转速
            zs = t[10]
            zs1 = int(zs)
            zs2 = hex(zs1)[2:].zfill(4)
            print('转速',zs2)
            # print(type(zs2))

            #定位状态
            dwzt = t[11]
            print(dwzt)
            # print(type(dwzt))

            #经度
            jingdu = t[12]
            jingdu1 = float(jingdu)*1000000
            jingdu2 = hex(int(jingdu1))[2:].zfill(8)
            print('经度',jingdu2)
            # print(type(jingdu2))

            #纬度
            weidu = t[13]
            weidu1 = float(weidu)*1000000
            weidu2 = hex(int(weidu1))[2:].zfill(8)
            print('纬度',weidu2)
            # print(type(weidu2))

            #排温2
            pw2 = t[14]
            pw21 = int(pw2)+40
            pw22 = hex(pw21)[2:].zfill(4)
            print('排温2',pw22)
            # print(type(pw22))

            #排温1
            pw1 = t[15]
            pw11 = int(pw1)+40
            pw12 = hex(pw11)[2:].zfill(4)
            print('排温1',pw12)
            # print(type(pw12))

            #压差
            yc = t[16]
            yc1 = int(yc)
            yc2 = hex(yc1)[2:].zfill(4)
            print('压差',yc2)
            # print(type(yc2))

            #作业时长
            zysc = int(t[17])
            zysc1 = hex(zysc)[2:].zfill(8)
            print('作业时长',zysc1)
            # print(type(zysc1))

            #预留
            yl1 = t[18]
            yl11 = yl1.zfill(8)
            print(yl11)
            # print(type(yl1))

            #工作状态
            gzzt = (t[19])
            gzzt1 = gzzt.zfill(2)
            print(gzzt1)
            # print(type(gzzt))

            #预留
            yl2 = t[20]
            yl21 = yl2.zfill(8)
            print(yl21)
            # print('预留2',yl2)
            # print(type(yl2))

            #预留
            yl3 = t[21]
            yl31 = yl3.zfill(8)
            print(yl31)
            # print('预留3',yl3)
            # print(type(yl3))

            #预留
            yl4 = t[22]
            yl41 = yl4.zfill(8)
            print(yl41)
            # print('预留4',yl4)
            # print(type(yl4))

            #里程
            lc = t[23]
            lc1 = (int(lc))*10
            lc2 = hex(lc1)[2:].zfill(8)
            print('里程',lc2)
            # print(type(lc2))

            #补充位
            bcw = t[24]
            print(bcw)
            # print(type(bcw))

            #47、光吸收系数
            gxsxs = t[25]
            gxsxs1 = int(gxsxs) * 100
            gxsxs2 = hex(gxsxs1)[2:].zfill(4)
            print(gxsxs2)
            # print(type(gxsxs2))

            #48、不透光度
            btgd = t[26]
            btgd1 = int(btgd) * 10
            btgd2 = hex(btgd1)[2:].zfill(4)
            print(btgd2)
            # print(type(btgd2))

            #49、颗粒物浓度
            klwnd = t[27]
            klwnd1 = int(klwnd) * 10
            klwnd2 = hex(klwnd1)[2:].zfill(4)
            print(klwnd2)
            # print(type(klwnd2))

            w = sbw+mldy1+clsbh+rjbbh1+jm1+sjdycd+ti10+llh1+liushuihao1+sd2+zs2+dwzt+jingdu2+weidu2+pw22+pw12+yc2+zysc1+yl11+gzzt1+yl21+yl31+yl41+lc2+bcw+gxsxs2+btgd2+klwnd2


            # w = sbw+mldy1+clsbh+rjbbh1+jm1+sjdycd+ti10+llh+sd+zs1+dwzt+jingdu2+weidu2+pw22+pw11+yc1+zysc1+yl1+gzzt+yl2+yl3+yl4+lc2+bcw+gxsxs2+btgd2+klwnd2


            print(w)

            #组合校验
            data = w
            a = diaoyongjar.get_xor(data)
            b = diaoyongjar.get_bcc(a).zfill(2)
            # print(b)
            s = w + b
            print(s)

            #发送
            t = a + ' ' + b
            print(t)
            # s.send(bytes().fromhex(sj))
            s = socket(AF_INET, SOCK_STREAM)
            # s.connect(('120.77.17.210',7020)) #测试
            # s.connect(('120.77.133.46', 8010))  # 开发
            s.connect(('47.113.58.88',7020)) #正式
            # s.connect(('106.112.219.162', 8010))  # 泊头
            # s.connect(('47.106.76.236', 8010))  # docker
            # s.connect(('120.77.17.210', 7020))  # 非道路

            s.send(bytes().fromhex(t))
            print('\n' * 1)
            time.sleep(1)
            # s.close()

if __name__ == '__main__':
    ll = login()
    ll.get(2,1)

    # while True:
    #     time.sleep(5)
    #     oo = login()
    #     oo.get(2,1)








