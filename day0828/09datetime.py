# 09datetime.py

import datetime  #from  import 
import time

# 에러 x = datetime.now()  

y = datetime.datetime.now() #정답
print(y)      #2024-08-28 11:18:20.641497
print(str(y)) #안전화  
z = str(y)
print(z[0:4]) #2024-2001 = 나이 계산
print()

dt = datetime.datetime.now() 
print(dt.strftime('%Y년-%m월-%d일') )
print(dt.strftime('%H시-%M분-%S초') )
print()

mytime = time.localtime()
print(mytime)
print(mytime.tm_year) # 2024년도 나이계산
'''
2024-08-28 13:34:57.169864
2024-08-28 13:34:57.169864
2024

2024년-08월-28일
13시-34분-57초

time.struct_time(tm_year=2024, tm_mon=8, tm_mday=28, tm_hour=13, tm_min=34, tm_sec=57, tm_wday=2, tm_yday=241, tm_isdst=0)
2024
'''