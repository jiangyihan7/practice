# -*- coding: utf-8 -*-
#输入整数，其二进制中1的个数

#对二进制数进行右移操作，每次右移一位，然后和1进行与运算。

def count_1(a):
    # 二进制数存储在计算机中的是补码,32是计算机的位数
     return sum([(a>>i)&1 for i in range(32)])
print(count_1(5))