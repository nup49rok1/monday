#08testdatetime.py

import time
import datetime  #datetime.datetime.now()으로 접근함
# from 파일명클래스 import datetime

#from datetime import datetime  #datetime.now() 으로 접근함

#dt = datetime.now()  #에러유발
#AttributeError: module 'datetime' has no attribute 'now' 

my = time.localtime()
print(my) #구조가 복잡
print(my.tm_year,'년')#2024
print(my.tm_mon,'월')#8
print(my.tm_mday,'일')
print(my.tm_wday) #0(월) 1(화) 2(수) 3(목) 4(금)=>숫자로 출력이 됨
time.sleep(0.5)
print()

dt = datetime.datetime.now()
print(dt) #2024-08-23 11:15:29.369918 2024-08-23 11:16:16.686176

time.sleep(0.5)
print('aaaaaaa')
time.sleep(0.5)
print('bbbbbbb')
time.sleep(0.5)
print('ccccccc')
'''
8testdatetime.py
time.struct_time(tm_year=2024, tm_mon=8, tm_mday=23, tm_hour=11, tm_min=51, tm_sec=7, tm_wday=4, tm_yday=236, tm_isdst=0)
2024 년
8 월
23 일
4

2024-08-23 11:51:07.769642
aaaaaaa
bbbbbbb
ccccccc
'''