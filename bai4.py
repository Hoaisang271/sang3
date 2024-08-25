# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:38:35 2024

@author: Student
"""

x=int(input('Nhập vào số giây:'));
gio = x//3600;
x=x%3600;
phut=x//60;
x=x%60;
print('Kết quả =', gio,'giờ:', phut, 'phút:', x,'giây');