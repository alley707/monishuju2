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
print(cs)
cs1 = int(cs,16)
cs2 = cs1*1/256
if cs == str('FFFF'):
    print('车速无效')
else:
    print('车速',cs2)

dqy = s[70:72]
dqy1 = int(dqy,16)
dqy2 = dqy1/2
if dqy == str('FF'):
    print('大气压无效')
else:
    print('大气压',dqy2)


fdjnj = s[72:74]
fdjnj1 = int(fdjnj,16)
fdjnj2 = fdjnj1-125
if fdjnj == str('FF'):
    print('发动机扭矩无效')
else:
    print('发动机扭矩',fdjnj2)

mcnj = s[74:76]
mcnj1 = int(mcnj,16)
mcnj2 = mcnj1-125
if mcnj == str('FF'):
    print('摩擦扭矩无效')
else:
    print('摩擦扭矩',mcnj2)

fdjzs = s[76:80]
fdjzs1 = int(fdjzs,16)
fdjzs2 = fdjzs1*1/8
if fdjzs == str('FFFF'):
    print('发动机转速无效')
else:
    print('发动机转速',fdjzs2)

fdjrl = s[80:84]
print(fdjrl)
fdjrl1 = int(fdjrl,16)
fdjrl2 = fdjrl1*1/20
if fdjrl == str("FFFF"):
    print('发动机燃料无效')
else:
    print('发动机燃料',fdjrl2)

scrup = s[84:88]
scrup1 = int(scrup,16)
scrup2 = scrup1*1/20
scrup3 = scrup2-200
if scrup == str("FFFF"):
    print('nox上游数据无效')
elif scrup == str('FFF0'):
    print('nox上游数据FFF0无效')
else:
    print('nox上',scrup3)

scrdw = s[88:92]
scrdw1 = int(scrdw,16)
scrdw2 = scrdw1*1/20
scrdw3 = scrdw2-200
print(scrdw)
if scrdw == str("FFFF"):
    print('nox下游数据无效')
elif scrdw == str('FFF0'):
    print('nox下游数据FFF0无效')
else:
    print('nox下',scrdw3)

fyjyl = s[92:94]
fyjyl1 = int(fyjyl,16)
fyjyl2 = fyjyl1*2/5
print(fyjyl)
if fyjyl == str("FF"):
    print('反应剂余量数据无效')
else:
    print('反应剂余量',fyjyl2)

jq = s[94:98]
jq1 = int(jq,16)
jq2 = jq1*1/20
if jq == str("FFFF"):
    print('进气数据无效')
else:
    print('进气',jq2)

rkwd = s[98:102]
rkwd1 = int(rkwd,16)
rkwd2 = rkwd1*1/32
rkwd3 = rkwd2-273
if rkwd == str("FFFF"):
    print('入口温度数据无效')
else:
    print('入口温度',rkwd3)

ckwd = s[102:106]
ckwd1 = int(ckwd,16)
ckwd2 = ckwd1*1/32
ckwd3 = ckwd2-273
if ckwd == str("FFFF"):
    print('出口温度数据无效')
else:
    print('出口温度',ckwd3)

dpfyc = s[106:110]
dpfyc1 = int(dpfyc,16)
dpfyc2 = dpfyc1/10
if dpfyc == str("FFFF"):
    print('pdf压差数据无效')
else:
    print('pdf压差',dpfyc2)

fdjwd = s[110:112]
fdjwd1 = int(fdjwd,16)
fdjwd2 = fdjwd1-40
if fdjwd == str("FF"):
    print('发动机温度数据无效')
else:
    print('发动机温度',fdjwd2)

yxyw = s[112:114]
yxyw1 = int(yxyw,16)
yxyw2 = yxyw1*2/5
if yxyw == str("FF"):
    print('油箱液位数据无效')
else:
    print('油箱液位',yxyw2)

dwzt = s[114:116]
print(dwzt)
if dwzt == str('00'):
    print('定位状态有效')
elif dwzt == str('01'):
    print('定位状态无效')
else:
    print('未知定位状态',dwzt)



jd = s[116:124]
jd1 = int(jd,16)
jd2 = jd1/1000000
print(jd)
if jd == str("FFFFFFFF"):
    print('经度数据无效')
else:
    print('经度',jd2)

wd = s[124:132]
wd1 = int(wd,16)
wd2 = wd1/1000000
print(wd)
if wd == str("FFFFFFFF"):
    print('纬度数据无效')
else:
    print('纬度',wd2)

lc = s[132:140]
lc1 = int(lc,16)
lc2 = lc1/10
print(lc)
if lc == str("FFFFFFFF"):
    print('里程数据无效')
else:
    print('里程',lc2)

bcw = s[140:142]
if bcw == "80":
    print('补充位',bcw)
else:
    os._exit(0)

fdjnjms = s[142:144]
fdjnjms1 = int(fdjnjms,16)
if fdjnjms1 == 0:
    print('发动机扭矩模式:超速失效')
elif fdjnjms1 == 1:
    print('发动机扭矩模式:转速控制')
elif fdjnjms1 == 2:
    print('发动机扭矩模式:扭矩控制')
elif fdjnjms1 == 3:
    print('发动机扭矩模式:转速/扭矩控制')
elif fdjnjms1 == 9:
    print('发动机扭矩模式:正常')
elif fdjnjms == str('FF'):
    print('发动机扭矩模式无效')


ymtb = s[144:146]
ymtb1 = int(ymtb,16)
ymtb2 = ymtb1*2/5
if ymtb == str("FF"):
    print('油门踏板数据无效')
else:
    print('油门踏板',ymtb2)

ljyh = s[146:154]
ljyh1 = int(ljyh,16)
ljyh2 = ljyh1
ljyh3 = ljyh2/1000
print(ljyh)
if ljyh == str("FFFFFFFF"):
    print('累计油耗数据无效')
else:
    print('累计油耗',ljyh3)

nsxwd = s[154:156]
nsxwd1 = int(nsxwd,16)
nsxwd2 = nsxwd1-40
print(nsxwd)
if nsxwd == str("FF"):
    print('尿素箱温度数据无效')
else:
    print('尿素箱温度',nsxwd2)

sjnspsl = s[156:164]
sjnspsl1 = int(sjnspsl,16)
sjnspsl2 = sjnspsl1/100
print(sjnspsl)
if sjnspsl == str("FFFFFFFF"):
    print('实际尿素喷射量数据无效')
else:
    print('实际尿素喷射量',sjnspsl2)

ljnspsl = s[164:172]
ljnspsl1 = int(ljnspsl,16)
ljnspsl2 = ljnspsl1
print(ljnspsl)
if ljnspsl == str("FFFFFFFF"):
    print('累计尿素喷射量数据无效')
else:
    print('累计尿素喷射量',ljnspsl2)

dpfwd = s[172:176]
dpfwd1 = int(dpfwd,16)
dpfwd2 = dpfwd1*1/32
if dpfwd == str("FFFF"):
    print('dpf排气温度数据无效')
else:
    print('dpf排气温度',dpfwd2)



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




