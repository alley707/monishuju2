# _*_ coding:utf-8 _*_

import os
s = input ('输入数据:')

jyw = s[0:4]
print ('校验位',jyw)

sjlx = s[4:6]
print('数据类型',sjlx)

sbh = s[6:40]
print('设备号',sbh)

zdbbh = s[40:42]
print('终端版本号',zdbbh)

jm = s[42:44]
print('加密',jm)

sjcd = s[44:48]
sjcd1 = int(sjcd,16)
print('数据长度',sjcd1)

sj = s[48:60]
print(sj)
sj1 = int(sj[0:2],16)
sj2 = int(sj[2:4],16)
sj3 = int(sj[4:6],16)
sj4 = int(sj[6:8],16)
sj5 = int(sj[8:10],16)
sj6 = int(sj[10:12],16)
sj7 =(str(sj1)+'年'+str(sj2)+'月'+str(sj3)+'日'+str(sj4)+'时'+str(sj5)+'分'+str(sj6))+'秒'
print('时间',sj7)

sjlxbz = s[60:62]
print('数据类型标志',sjlxbz)

xxlsh = s[62:66]
print('信息流水号',xxlsh)

cs = s[66:70]
cs1 = int(cs,16)
cs2 = cs1 * 1/256
if cs == "FFFF":
    print("车速无效")
else:
    print('车速',cs2)

zs = s[70:74]
print('转速',zs)

dwzt = s[74:76]
dwzt1 = bin(int(dwzt))[2:]
print(dwzt1)

jd = s[76:84]
jd1 = int(jd,16)
jd2 = jd1/1000000
print(jd)
if jd == str("FFFFFFFF"):
    print('经度数据无效')
else:
    print('经度',jd2)

wd = s[84:92]
wd1 = int(wd,16)
wd2 = wd1/1000000
print(wd)
if wd == str("FFFFFFFF"):
    print('纬度数据无效')
else:
    print('纬度',wd2)

pw2 = s[92:96]
pw21 = int(pw2,16) - 40
print('排温2',pw21)

pw1 = s[96:100]
pw11 = int(pw1,16) - 40
print('排温1',pw11)

yc = s[100:104]
yc1 = int(yc,16)
print('压差',yc1)

zysc = s[104:112]
zysc1 = int(zysc,16)
print("作业时长",zysc1)

yl1 = s[112:120]
print("预留1",yl1)

zgzt = s[120:122]
if zgzt == "01":
    print('运动中')
elif zgzt == "00":
    print("停止")
elif zgzt == '02':
    print('作业中')

yl2 = s[122:130]
print("预留2",yl2)

yl3 = s[130:138]
print("预留3",yl3)

yl4 = s[138:146]
print("预留4",yl4)

ljlc = s[146:154]
ljlc1 = int(ljlc,16)/10
print('累计里程',ljlc1,'km')


# gxsxs = s[172:176]
# gxsxs1 = int(gxsxs,16)
# gxsxs2 = gxsxs1/100
# if gxsxs == str("FFFF"):
#     print('光吸收系数数据无效')
# else:
#     print('光吸收系数',gxsxs2)
#
# btgd = s[176:180]
# btgd1 = int(btgd,16)
# btgd2 = btgd1/10
# if btgd == str("FFFF"):
#     print('不透光度数据无效')
# else:
#     print('不透光度',btgd2)
#
# klwnd = s[180:184]
# print(klwnd)
# klwnd1 = int(klwnd,16)
# klwnd2 = klwnd1/10
# if klwnd == str("FFFF"):
#     print('颗粒物浓度数据无效')
# else:
#     print('颗粒物浓度',klwnd2)
