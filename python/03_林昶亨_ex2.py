# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:18:07 2020

@author: ASUS
"""

#定義"a的b次方"之函式
def compute(a, b):
    ans = a**b
    return ans

#使用者輸入a, b
st= eval(input("請輸入a:"))
nd= eval(input("請輸入b:"))

#呼叫compute函式
answer = compute(st, nd)

#輸出結果
print("a的b次方為:",answer)