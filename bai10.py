# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:15:59 2024

@author: Student
"""

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = "I'm a cat"
  
print("Chuỗi ban đầu là : ", end="")
print(s)
  
print("Chuỗi đã được đảo ngược (sử dụng vòng lặp) là : ", end="")
print(reverse(s))
