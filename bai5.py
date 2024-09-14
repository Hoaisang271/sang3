# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:49:49 2024

@author: Student
"""

namsinh = int(input("Nhap nam sinh cua ban: "))
namhientai = 2023
tuoi = namhientai - namsinh
if tuoi == 0:
    print("Tuoi cua ban la: ")
elif (tuoi < 0 ):
    print(" Tuoi chua ton tai ")
else:
    print("tuoi cua ban la:  ", namhientai - namsinh)
    
    
    
