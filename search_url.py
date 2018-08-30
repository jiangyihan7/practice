# -*- coding: utf-8 -*-
'''
将 http://www.360.cn/ 另存为本地文件，编写
代码找出文件中所有的URL并保存到文件里

'''
import re,requests
url='https://www.360.cn/'
r=requests.get(url)
r.encoding='utf-8'

file=open('webpage','w',encoding='utf-8')
file.write(r.text)

f=open('webpage','r',encoding='utf-8')
s=f.read()
results=re.findall("(http\://[a-zA-Z0-9\.\?\&\=\:]+)",s)
print(results)
aa='\n'.join(results)
ff=open('result.txt','w')
ff.write(aa)
