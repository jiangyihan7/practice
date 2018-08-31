# -*- coding: utf-8 -*-

'''
编写代码找出 C:\Program Files (x86)\360\360Safe
      目录下所有的.ini文件（包括子目录下的文件）

'''
import os
path=r'C:\Program Files (x86)\360\360Safe'
result=[]
for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith('ini'):
            result.append(file)
r='\n'.join(result)
print(r)
print(len(result))
