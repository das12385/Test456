# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:17:12 2020

@author: ASUS
"""

#使用者輸入
a = input("請輸入一個正整數:")

#判斷是否正整數
while a.isdigit() == False or a == "0":
    a = input("輸入錯誤，請重新輸入一個正整數:")

#設定預設值
i = 1
count = 0

#while迴圈計算
while i<=int(a) :
    if i%7 == 0:
        count += i
    i += 1
#輸出結果
print("(while)從1到"+a+"中7的倍數總和是:"+str(count))

#設定預設值
i = 1
count = 0

#for迴圈計算
for i in range(1, int(a)+1):
    if i%7 == 0:
        count += i
    i += 1
#輸出結果   
print("(for)從1到"+a+"中7的倍數總和是:"+str(count))    
