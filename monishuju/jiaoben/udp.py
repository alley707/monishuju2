# _*_ coding:utf-8 _*_
import socket
import multiprocessing
import time
from multiprocessing import Pool


def ss(self):
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    m = 0
    n = 1
    while m < 100:
        # s.sendto(
        #     "<TXT*S:13533553032*VIN:LZZ1CLXC4KA552904*T:14*NOX:0.000,3076.000*UP:1,5,0,1;*C:31*CL:1,460,0,3BA4C00,24,37900,38,3773*W:121*PM:10101,0,810*O:1270/86,247/0,351/0*3I:41-16,0.0(34.6588,113.6759)3D8,0*SN:34,33,32,31,31*4D:0,0,4837*A:4114,2565*3G:TB02_FA33_V1.14*IC:L016AB0100.0058*NW:31,299,23*INF:6.48.0.79.A0.2-2*MD:0,0*SEID:BFCHB14146106236>".encode(),
        #     ("47.106.76.236", 4542))
        k = "<TXT*S:"
        l = 14633553040
        c = l + n
        t = "*VIN:LZZ1CLXC4KA552904*T:14*NOX:0.000,3076.000*UP:1,5,0,1;*C:31*CL:1,460,0,3BA4C00,24,37900,38,3773*W:121*PM:10101,0,810*O:1270/86,247/0,351/0*3I:41-16,0.0(34.6588,113.6759)3D8,0*SN:34,33,32,31,31*4D:0,0,4837*A:4114,2565*3G:TB02_FA33_V1.14*IC:L016AB0100.0058*NW:31,299,23*INF:6.48.0.79.A0.2-2*MD:0,0*SEID:BFCHB14146106236>"
        o = str(k + str(c) + t)
        s.sendto(o.encode(),("47.113.58.88", 4542))
        m += 1
        n += 1
        if m == 100:
            break
        print(m)
        print(o)

if __name__ == '__main__':
    pool = Pool(processes = 4)
    for i in range(10):
        pool.apply_async(ss, args=(i,))
    print('======  apply_async  ======')
    pool.close()
    pool.join()



    # ll = sock()
    # ll.ss()
    # p1 = [multiprocessing.Process(target = ll.ss(),args=('anne',)),multiprocessing.Process(target = ll.ss(),args=('haha',))]
    # for t in p1:
    #     t.start()
    #     t.join()






