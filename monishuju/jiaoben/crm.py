# _*_ coding:utf-8 _*_

def crc16(strbuf, lenth):
    result = 0
    tempcrc16 = 0
    tempdata = 0
    m = 0
    n = 0
    result = result
    for m in range(lenth):
        result = (result & 0xFFFF)  # 因为Python的int整形数没有最大值，所以需要&上0xffff
        tempcrc16 = (tempcrc16 & 0xFFFF)  # 因为Python的int整形数没有最大值，所以需要&上0xffff
        tempdata = (tempdata & 0xFFFF)  # 因为Python的int整形数没有最大值，所以需要&上0xffff
        tempcrc16 = (((result >> 8) ^ strbuf[m]) & 0xffff)
        tempdata = (tempcrc16 << 8)
        tempcrc16 = 0

        for n in range(8):
            if ((tempdata ^ tempcrc16) & 0x8000):
                tempcrc16 = (((tempcrc16 << 1)) ^ 0x1021)
            else:
                tempcrc16 = (tempcrc16 << 1)
            tempdata = (tempdata << 1)
        # print(tempcrc16)
        result = ((result << 8) ^ tempcrc16)

    return result
# if __name__ == '__main__':



buf = [0x78,0x78,0x11,0x01,0x08,0x63,0x65,0x60,0x40,0x21,0x80,0x39,0x01,0x00,0x32,0x00,0x00,0x00,0x21,0xAD]

print(crc16(buf, len(buf)))  # 6695815

t = (crc16(buf, len(buf)) & 0xff)
print(int(t)) # 135

print(((crc16(buf, len(buf)) >> 8) & 0xff))  # 43
