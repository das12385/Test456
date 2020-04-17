# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 09:10:31 2020

@author: ASUS
"""

def attack(normal, ex, square):
    n2 = normal
    e2 = ex*2
    s2 = square*1.5
    return n2, e2, s2
n1=eval(input("請輸入普通攻刃:"))
e1=eval(input("請輸入ex攻刃:"))
s1=eval(input("請輸入方陣攻刃:"))
n,e,s = attack(n1,e1,s1)
print("普通攻刃=",n,
      "ex攻刃=",e,
      "方陣攻刃=",s)



