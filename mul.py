# -*- coding: utf-8 -*-
#大整数乘法的竖式计算过程

def mul(a,b):
    aa=list(map(int,reversed(str(a))))
    bb=list(map(int,reversed(str(b))))
    # n位整数和m位整数的乘积最多是n+m位整数
    result=[0]*(len(aa)+len(bb))
    for i,va in enumerate(aa):
        c=0 #进位
        for j,vb in enumerate(bb):
            c,result[i+j]=divmod(va*vb+c+result[i+j],10)
            print(c,result[i+j])
        result[i+j+1]=c

    result = int(''.join(map(str,reversed(result))))
    return result
