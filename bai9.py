# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:41:54 2024

@author: Student
"""
import math

# Nhập giá trị cho a và b
a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))

# Tính các thành phần của biểu thức
phan_1 = (math.sqrt(a) - math.sqrt(b)) / (4 * math.sqrt(math.sqrt(a)) - 4 * math.sqrt(math.sqrt(b)))
phan_2 = (math.sqrt(a) + math.sqrt(math.sqrt(a * b))) / (4 * math.sqrt(math.sqrt(a)) + 4 * math.sqrt(math.sqrt(b)))

# Tính giá trị biểu thức tổng
ket_qua = phan_1 - phan_2

# In kết quả
print(f"Kết quả: {ket_qua}")
4