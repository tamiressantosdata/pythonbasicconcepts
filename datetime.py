# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:58:04 2022

@author: tamir
"""

from datetime import datetime, date, time
dt = datetime(2022, 10, 29, 20, 30, 21)

print(dt.day)

print(dt.time())

print(dt.minute)
print(dt.date())

print(dt.strftime('%d/%m/%Y %H:%M'))