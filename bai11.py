# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:17:19 2024

@author: Student
"""

address = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = address.split(', ')

for sub in sub_strings:
    print(sub)
    import re

address = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

sub_strings = re.split(',\s*', address)

cleaned_strings = [re.sub(r'^(P\.|Q\.|Tp\.)\s*', '', sub) for sub in sub_strings]

for sub in cleaned_strings:
    print(sub)