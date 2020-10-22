# _*_ coding:utf-8 _*_
import csv
import os
import time
import diaoyongjar
from socket import *


# n = 1
# m = 1

class shujuzuhejiaoytbox:
    def get(self, nob, noc):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/excelFile/boyunshikong/boxbox/boxbox4.csv"
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

            #1、识别位
            sbw = t[0]
            # print(sbw)

            #2、命令单元
            mldy = t[1]
            mldy1 = mldy.zfill(2)
            # print(mldy1)

            #3、车辆识别号  bu
            clsbh1 = t[2]
            # clsbh1 = '3'+clsbh[0]+'3'+clsbh[1]+'3'+clsbh[2]+'3'+clsbh[3]+'3'+clsbh[4]+'3'+clsbh[5]+'3'+clsbh[6]+'3'+clsbh[7]+'3'+clsbh[8]+'3'+clsbh[9]+'3'+clsbh[10]+'3'+clsbh[11]+'3'+clsbh[12]+'3'+clsbh[13]+'3'+clsbh[14]+'3'+clsbh[15]+'3'+clsbh[16]
            print(clsbh1)

            #4、软件版本号
            rjbbh = t[3]
            rjbbh1 = rjbbh.zfill(2)
            # print(rjbbh1)

            #5、加密方式
            jmfs = t[4]
            jmfs1 = jmfs.zfill(2)
            # print(jmfs1)

            #6、长度
            sjcd = t[5]
            # print(sjcd)

            #7、时间[6]
            ti = time.strftime("%Y%m%d%H%M%S")
            ti2 = str(ti)
            ti3 = 2 * '' + ti2[2:]
            ti4 = (hex(int(ti3[0:2]))[2:4]).zfill(2)
            ti5 = (hex(int(ti3[2:4]))[2:4]).zfill(2)
            ti6 = (hex(int(ti3[4:6]))[2:4]).zfill(2)
            ti7 = (hex(int(ti3[6:8]))[2:4]).zfill(2)
            ti8 = (hex(int(ti3[8:10]))[2:4]).zfill(2)
            ti9 = (hex(int(ti3[10:12]))[2:4]).zfill(2)
            ti10 = ti4+ti5+ti6+ti7+ti8+ti9
            # ti11 = '130b13123808'
            print(ti10)

            #8、信息流水号
            xxlsh = t[7]
            # print(xxlsh)

            #9、信息类型
            sjlx = t[8]
            sjlx1 = sjlx.zfill(2)
            # print(sjlx1)

            #10、诊断协议
            zhenduanxy = t[9]
            zhenduanxy1 = zhenduanxy.zfill(2)
            # print(zhenduanxy1)

            #11、mil就绪
            mil = t[10]
            mil1 = mil.zfill(2)
            # print(mil1)

            #12、诊断支持状态
            zdzc = t[11]
            zdzc1 = zdzc.zfill(4)
            # print(zdzc1)

            #13、诊断就绪
            zdjx = t[12]
            zdjx1 = zdjx.zfill(4)
            # print(zdjx1)

            #14、车辆识别号  bu
            clsbh2 = t[13]
            # print(clsbh)

            #15、软件标定识别号
            # rjsbh = t[14]
            rjsbh = '303030303030303030303030303030303030'
            # print(rjsbh)

            #16、标定验证码
            # bdyzm = t[15]
            bdyzm = '303030303030303030303030303030303030'
            # print(bdyzm)

            #17、inpur值
            # inpur = t[16]
            inpur = '303030303030303030303030303030303030303030303030303030303030303030303030'
            # print(inpur)

            #18、故障码
            guzm = t[17]
            guzm1 = guzm.zfill(2)
            # print(guzm1)

            #19、数据流信息
            ljlx = t[18]
            ljlx1 = ljlx.zfill(2)
            # print(ljlx1)

            #20、车速
            sudu = t[19]
            sudu1 = int(sudu)*256
            sudu2 = hex(sudu1)[2:].zfill(4)
            print(sudu2)


            #21、大气压值
            dqy = t[20]
            dqy1 = int(float(dqy))*2
            dqy2 = hex(dqy1)[2:].zfill(2)
            # print(dqy2)

            #22、发动机扭矩
            fdjnj = t[21]
            fdjnj1 = int(fdjnj)+125
            fdjnj3 = hex(fdjnj1)[2:].zfill(2)
            # print(fdjnj3)

            #23、摩擦扭矩
            mcnj = t[22]
            mcnj1 = int(mcnj)+125
            mcnj2 = hex(mcnj1)[2:].zfill(2)
            # print(mcnj2)

            #24、发动机转速
            fdjzs = t[23]
            fdjzs1 = int(fdjzs)*8
            fdjzs2 = hex(fdjzs1)[2:].zfill(4)
            # print(fdjzs2)

            #25、发动机燃料流量
            fdjrlll = t[24]
            fdjrlll1 = int(fdjrlll)*20
            fdjrlll2 = hex(fdjrlll1)[2:].zfill(4)
            # print(fdjrlll2)

            #26、上nox
            unox = t[25]
            unox1 = int(unox)+200
            unox2 = unox1*20
            unox3 = hex(unox2)[2:].zfill(4)
            # print(unox3)

            #27、下nox
            dnox = t[26]
            dnox1 = int(dnox)+200
            dnox2 = dnox1*20
            dnox3 = hex(dnox2)[2:].zfill(4)
            # print(dnox3)

            #28、尿素箱液位
            fyjyl = t[27]
            fyjyl1 = float(fyjyl)*5/2
            fyjyl2 = hex(int(fyjyl1))[2:].zfill(2)
            # print(fyjyl)
            # print(fyjyl1)
            # print(fyjyl2)



            #29、进气量
            jinqil = t[28]
            jinqil1 = int(jinqil)*20
            jinqil2 = hex(jinqil1)[2:].zfill(4)
            # print(jinqil2)

            #30、scr入口温度
            iwd = t[29]
            iwd1 = int(iwd)+273
            iwd2 = float(iwd1)/0.03125
            iwd3 = hex(int(iwd2))[2:].zfill(4)
            # print(iwd3)

            #31、scr出口温度
            owd = t[30]
            owd1 = int(owd)+273
            owd2 = float(owd1)/0.03125
            owd3 = hex(int(owd2))[2:].zfill(4)
            # print(owd3)

            #32、dpf压差
            DPFyc = t[31]
            DPFyc1 = int(DPFyc)*10
            DPFyc2 = hex(DPFyc1)[2:].zfill(4)
            # print(DPFyc2)

            #33、发动机冷却液温度
            lqwd = t[32]
            lqwd1 = int(lqwd)+40
            lqwd2 = hex(lqwd1)[2:].zfill(2)
            # print(lqwd2)

            #34、油箱液位
            yw = t[33]
            yw1 = float(yw)*2.5
            yw2 = hex(int(yw1))[2:].zfill(2)
            # print(yw2)

            #35、定位状态
            dw = t[34]
            dw1 = (dw).zfill(2)
            # print(dw1)

            #36、纬度
            weidu = t[35]
            weidu1 = float(weidu)*1000000
            weidu2 = hex(int(weidu1))[2:].zfill(8)
            # print(weidu2)

            #37、经度
            jingdu = t[36]
            jingdu1 = float(jingdu)*1000000
            jingdu2 = hex(int(jingdu1))[2:].zfill(8)
            # print(jingdu2)

            #38、里程
            lichen = t[37]
            # lichen1 = (int(lichen))*10
            lichen1 = (int(lichen))*10
            lichen2 = hex(lichen1)[2:].zfill(8)
            # print(lichen2)

            #39、补充位
            buchong = t[38]
            buchong1 = buchong.zfill(2)
            # print(buchong1)

            #40、扭矩模式
            niuju = t[39]
            niuju1 = niuju.zfill(2)
            # print(niuju1)

            #41、油门踏板
            taban = t[40]
            taban1 = float(taban)*2.5
            taban2 = hex(int(taban1))[2:].zfill(2)
            # print(taban2)

            #42、累计油耗
            youhao = t[41]
            # youhao1 = (int(youhao))
            youhao1 = (int(youhao))
            youhao2 = hex(youhao1)[2:].zfill(8)
            # print(youhao2)

            #43、尿素箱温度
            nswd = t[42]
            nswd1 = int(nswd)+40
            nswd2 = hex(nswd1)[2:].zfill(2)
            # print(nswd2)

            #44、实际尿素喷射量
            shijipsl = t[43]
            shijipsl1 = float(shijipsl) *100
            shijipsl2 = hex(int(shijipsl1))[2:].zfill(8)
            # print(shijipsl2)

            #45、累计尿素喷射量
            leijipeishel = t[44]
            leijipeishel1 = hex(int(leijipeishel))[2:].zfill(8)
            # print(leijipeishel1)

            #46、pdf排气温度
            pdfpqwd = t[45]
            pdfpqwd1 = float(pdfpqwd)+273
            pdfpqwd2 = float(pdfpqwd1)/0.03125
            pdfpqwd3 = hex(int(pdfpqwd2))[2:].zfill(4)
            # print(pdfpqwd3)

            #47、光吸收系数
            gxsxs = t[46]
            gxsxs1 = int(gxsxs) * 100
            gxsxs2 = hex(gxsxs1)[2:].zfill(4)

            #48、不透光度
            btgd = t[47]
            btgd1 = int(btgd) * 10
            btgd2 = hex(btgd1)[2:].zfill(4)

            #49、颗粒物浓度
            klwnd = t[48]
            klwnd1 = int(klwnd) * 10
            klwnd2 = hex(klwnd1)[2:].zfill(4)


            w = sbw+mldy1+clsbh1+rjbbh1+jmfs1+sjcd+ti10+sjlx1+xxlsh+zhenduanxy1+mil1+zdzc1+zdjx1+clsbh2+rjsbh+bdyzm+inpur+guzm1+ljlx1+sudu2+dqy2+fdjnj3+mcnj2+fdjzs2+fdjrlll2+unox3+dnox3+fyjyl2+jinqil2+iwd3+owd3+DPFyc2+lqwd2+yw2+dw1+jingdu2+weidu2+lichen2+buchong1+niuju1+taban2+youhao2+nswd2+shijipsl2+leijipeishel1+pdfpqwd3+gxsxs2+btgd2+klwnd2

            # w = sbw+mldy1+clsbh+rjbbh1+jmfs1+sjcd+ti10+sjlx1+xxlsh+zhenduanxy1+mil1+zdzc1+zdjx1+clsbh+rjsbh+bdyzm+inpur+guzm1+ljlx1+sudu2+dqy2+fdjnj3+mcnj2+fdjzs2+fdjrlll2+unox3+dnox3+fyjyl2+jinqil2+iwd3+owd3+DPFyc2+lqwd2+yw2+dw1+jingdu2+weidu2+lichen2+buchong1+niuju1+taban2+youhao2+nswd2+shijipsl2+leijipeishel1+pdfpqwd3
            # print(w)

            #组合校验
            data = w
            a = diaoyongjar.get_xor(data)
            b = diaoyongjar.get_bcc(a).zfill(2)

            # s = w + b
            # print(s)

            #发送
            t = a + ' ' + b
            # t = "787811010863656040211380010032000000E1A70D0A"
            # t = '23230242534A435331323334353637383931343702010046140903132004020006FFFF007D7D000000000FA00FA0000000222022200000280001FFFFFFFFFFFFFFFF00000000800000000000002800000000000000002220000000000000A1'
            # t = '23 23 02 35 35 36 36 35 35 36 36 35 35 36 36 35 35 36 36 34 02 01 00 69 14 09 18 0a 3a 2c 01 00 03 00 00 00 00 00 00 4C 5A 47 43 52 32 52 36 30 4C 58 30 33 37 36 32 35 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 00 70'
            # print(t)
            # s.send(bytes().fromhex(sj))
            s = socket(AF_INET, SOCK_STREAM)
            # s.connect(('120.77.17.210',8010)) #测试
            # s.connect(('120.77.133.46', 8010))  # 开发
            s.connect(('47.113.58.88',8010)) #正式
            # s.connect(('106.112.219.162',8010)) #泊头
            # s.connect(('154.8.163.218', 8010))  #docker
            # s.connect(('47.106.76.236', 31997))  #docker
            # s.connect(('116.62.230.113', 9200))  #d
            # s.connect(('192.168.130.208', 8010))  #d

            s.send(bytes().fromhex(t))
            print('\n' * 1)
            # time.sleep(10)
            # s.close()






if __name__ == '__main__':
    ll = shujuzuhejiaoytbox()
    ll.get(2,1)





    # m+=10
    # n+=5000
    # m = 1
    # while True:
    #     m+=1
    #     print('发送第%d条' %m)
    #     gg = shujuzuhejiaoytbox()
    #     gg.get(2,1)
    #     # time.sleep(10)













