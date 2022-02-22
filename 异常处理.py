# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:03:26 2022

@author: vv123
"""
while True:
    try:
        num1, num2 = map(int, input().split())
        print(num1 / num2)
    except Exception as err:
        print('something wrong:', err)
    else: 
        print("Everything is OK.")
        break
    finally:
        print('qwq')
        
try:        
    with open('datb.txt') as f:
        for line in f:
            print(line)
except Exception as err:
    print("failed:", err)