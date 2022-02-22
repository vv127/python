# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:13:44 2022

@author: vv123
"""

import requests
import re
r = requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.3347944549060917&callback=jQuery1112045097559680238364_1645492310053&_=1645492310055')
content = r.text.encode('utf-8').decode('unicode-escape')
reg = r"\"title\":\"(.*?)\""
result = re.findall(reg, content)
file = open('output.txt', 'w', encoding='utf-8')
for i in range(len(result)):
    print(i + 1, result[i])