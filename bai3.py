# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:24:23 2024

@author: Student
"""

n = int(input("Nhap so nguyen duong N co 2 chu so: "))
if 10<=n<=99:
    a = n //10
    b = n % 10
    print("Tong cac chu so nguyen duong N:", a + b)
    
else:
    print("Chi nhap so co 2 chu so")
    
    