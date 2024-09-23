#08jumin.py

import datetime #from import 
import time

# x = datetime.now() #에러 발생->실행시
# print(x)

jumin = '011230-3835064'
jum1 = '971230'  #len() 6자릿수 체크
jum2 = '18350642' #len() 7자릿수 체크

# len1 = jum1.len() => #len(jum1)  수정해서 자릿수 체크할것.
# len2 = jum2.len() => #len(jum2)

#if jum1.len()

y = datetime.datetime.now() #정답
print(y) #2024-08-28 11:18:17.609969
print(str(y)) #안전화 2024 추출
z = str(y)
print(z[0:4]) #2024-2001 = 나이 계산
print()

dt = datetime.datetime.now() 
print(dt.strftime('%Y년-%M월-%d일'))#M 분 d
print(dt.strftime('%H시-%M분-%S초'))


mytime = time.localtime()
print(mytime)
print(mytime.tm_year)# 2024년도,나이 계산  (객체명.속성)

'''
2024-08-28 13:31:46.571354
2024-08-28 13:31:46.571354
2024

2024년-31월-28일
13시-31분-46초
time.struct_time(tm_year=2024, tm_mon=8, tm_mday=28, tm_hour=13, tm_min=31, tm_sec=46, tm_wday=2, tm_yday=241, tm_isdst=0)
2024

'''
'''
문자열을 주석처럼 사용 (최종 정리)

dt = datetime.datetime.now() #정답
print(str(dt)[0:4])  #2024-2001 = 나이계산
mytime = time.localtime()
print(mytime.tm_year) #2024-2001 =  나이계산

'''