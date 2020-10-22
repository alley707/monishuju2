#  -*- coding:utf-8 -*-
import time


class zuhejiaoyan(object):
    # 29协议校验
    @staticmethod
    def jiaoyan29(data):
        data_b = bytes().fromhex(data)
        n = len(data_b)
        b = data_b[0]
        for i in range(1, n - 2):
            b ^= data_b[i]
        array = []
        for a in data_b:
            array.append(a)
        array[n - 2] = b
        st = ""
        for j in array:
            ss = str(hex(j))[2:]
            sz = ss.zfill(2)
            st = st + sz
        st = st.upper()
        return st

    # 设备号转伪ip
    @staticmethod
    def shebeihao2Vip(sSim):
        if sSim is None or sSim == "":
            return None
        try:
            sTemp = []
            sIp = []
            if len(sSim) == 11:
                sTemp.append(int(sSim[3:5]))
                sTemp.append(int(sSim[5:7]))
                sTemp.append(int(sSim[7:9]))
                sTemp.append(int(sSim[9:11]))
                iHigt = int(sSim[1:3]) - 30
            elif len(sSim) == 10:
                sTemp.append(int(sSim[2:4]))
                sTemp.append(int(sSim[4:6]))
                sTemp.append(int(sSim[6:8]))
                sTemp.append(int(sSim[8:10]))
                iHigt = int(sSim[0:2]) - 30
            elif len(sSim) == 9:
                sTemp.append(int(sSim[1:3]))
                sTemp.append(int(sSim[3:5]))
                sTemp.append(int(sSim[5:7]))
                sTemp.append(int(sSim[7:9]))
                iHigt = int(sSim[0:1])
            elif len(sSim) < 9:
                sSim = "140" + sSim.zfill(8)
                sTemp.append(int(sSim[3:5]))
                sTemp.append(int(sSim[5:7]))
                sTemp.append(int(sSim[7:9]))
                sTemp.append(int(sSim[9:11]))
                iHigt = int(sSim[1:3]) - 30
            else:
                return None
            if (iHigt & 0x8) != 0:
                sIp.append(sTemp[0] | 128)
            else:
                sIp.append(sTemp[0])
            if (iHigt & 0x4) != 0:
                sIp.append(sTemp[1] | 128)
            else:
                sIp.append(sTemp[1])
            if (iHigt & 0x2) != 0:
                sIp.append(sTemp[2] | 128)
            else:
                sIp.append(sTemp[2])
            if (iHigt & 0x1) != 0:
                sIp.append(sTemp[3] | 128)
            else:
                sIp.append(sTemp[3])
            ipstr = ""
            for ip in sIp:
                ss = str(hex(ip))[2:].zfill(2)
                ipstr += ss
            return ipstr.upper()
        except Exception as e:
            print("设备号转伪ip失败！原因：%s" % e)
            return None

    # 拼接29协议
    def pinjiejiaoyan(self, shebeihao, weidu, jingdu, sudu, fangxiang, dingwei, licheng, acc, baojing):
        # 伪ip
        Vip = self.shebeihao2Vip(shebeihao)
        # 时间
        ti = time.strftime("%Y%m%d%H%M%S")
        ti2 = str(ti)
        ti3 = 2 * '' + ti2[2:]
        # 纬度
        wd1 = weidu.split(".")
        wd2 = float("0." + wd1[1]) * 60
        wd3 = '%.3f' % wd2  # 保留3位小数
        wd4 = str(wd3).zfill(6).split(".")
        wd5 = wd1[0] + wd4[0] + wd4[1]
        wd = wd5.zfill(8)  # 左补0
        # 经度
        jd1 = jingdu.split(".")
        jd2 = float("0." + jd1[1]) * 60
        jd3 = '%.3f' % jd2  # 保留3位小数
        jd4 = str(jd3).zfill(6).split(".")
        jd5 = jd1[0] + jd4[0] + jd4[1]
        jd = jd5.zfill(8)
        jwd = wd + jd
        # 速度
        sd = sudu.zfill(4)
        # 方向
        fx = fangxiang.zfill(4)
        # 定位
        if baojing.find("终端主电源掉电报警") != -1:
            if dingwei.find("不定位") != -1:
                dw = "70"
            else:
                dw = "F0"
        else:
            if dingwei.find("不定位") != -1:
                dw = "78"
            else:
                dw = "F8"
        # 里程
        lc1 = str(hex(int(licheng)))
        lc = lc1[2:].zfill(6)
        # ACC 开关
        if acc.find("关") != -1:
            ac = "FE"
        else:
            ac = "7E"
        # 报警类型
        if baojing.find("超速报警") != -1:
            bj = "BC"
        elif baojing.find("劫警") != -1:
            bj = "7C"
        elif baojing.find("终端主电源掉电报警") != -1:
            bj = "FC"
        else:
            bj = "FC"
        jiaoyanqian = "2929800028" + Vip + ti3 + jwd + sd + fx + dw + lc + ac + bj + "0000001E000000000000C80D"
        jiaoyanhou = self.jiaoyan29(jiaoyanqian)
        return jiaoyanhou
