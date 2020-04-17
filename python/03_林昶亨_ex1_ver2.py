# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:02:45 2020

@author: ASUS
"""

def isdec(y):
    if y.count(".") == 1:
        sl = y.split(".")
        left = sl[0]
        right = sl[1]
        if left.isdigit() == True and right.isdigit() == True:
            return True;
        else :
            return False;
    else :
        return False;
    

x0 = input("請輸入矩形的一邊:")
while x0.isdigit() != True and isdec(x0) != True:
    x0 = input("輸入錯誤，請重新輸入矩形的一邊:")
else:
    x1 = float(x0)


  
x2 = input("請輸入矩形的另一邊:")
while x2.isdigit() != True and isdec(x2) != True:
    x2 = input("輸入錯誤，請重新輸入矩形的一邊:")
else:
    x3 = float(x2)


if x1>x3:
   l=x1
   w=x3
   print("\n矩形的長為:",int(l))
   print("\n矩形的寬為:",int(w))
   print("\n矩形的周長為:",int(l*2+w*2))
   print("\n矩形的面積為:",int(l*w))
elif x1<x3:
     w=x1
     l=x3
     print("\n矩形的長為:",int(l))
     print("\n矩形的寬為:",int(w))
     print("\n矩形的周長為:",int(l*2+w*2))
     print("\n矩形的面積為:",int(l*w))
else :
     w=x1
     l=x3
     print("\n矩形四邊長皆為",int(l))
     print("\n矩形的周長為:",int(l*4))
     print("\n矩形的面積為:",int(l*w))
     

