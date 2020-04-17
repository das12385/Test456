# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:21:36 2020

@author: ASUS
"""

#使用者輸入
inputnum = input("請輸入一個整數:")

#判斷是否為整數
while inputnum.isdigit() != True:
    inputnum = input("輸入錯誤，請重新輸入一個整數:")
else :
    num = int(inputnum)
    
#判斷是否為2或7的倍數並輸出結果
if num%2 == 0 and num%7 == 0:
    print(num, "同時為2和7的倍數")
elif num%2 == 0 and num%7 != 0:
    print(num, "是2的倍數，但不是7的倍數")
elif num%2 != 0 and num%7 == 0:
    print(num, "是7的倍數，但不是2的倍數")
else:
    print(num, "不是2的倍數，也不是7的倍數")
