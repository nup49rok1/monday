# HWjumin.py.py

import datetime  #from  import 
import time

jumin = '971230-1835064' 

# 구현을 함수화
# split()사용 [시:끝+1]
# 문제1 if제어 성별체크   1/3 남자  2/4여자 
# 문제2 생일 12월30일 생일 축하합니다
# 문제3 나이계산 2024-1997 = 27
# 문제4 나중에 공개 

print()
print()

jum1 = '971230'  #len() 6자릿수 체크
jum2 = '18350642' #len() 7자릿수 체크
# len1 = jum1.len() len(jum1) 수정해서 자릿수체크
# len2 = jum2.len() len(jum2) 수정해서 자릿수체크


def sungCheck(jumin):
    if (jumin[7:8] == '1' or jumin[7:8] == '3'):
        print('당신은 남자입니다.')
    else:
        print('당신은 여자입니다.')
    print('-'*30)

#문제2

def birthd(jumin):
    mon=jumin[2:4]
    dy=jumin[4:6]
    print(f'당신의 생일은 {mon}월 {dy}일 이군요!' )
    print('-'*30)


#문제3 
def ageCheck(birthday):
    y = datetime.datetime.now() #정답
    z = str(y)
    print(f'당신의 나이는 {int(z[0:4])-birthday} 살입니다.') #2024-출생년도 = 나이 계산
    print()


def infoPrint():
    sungCheck('011230-3835064')
    sungCheck('0110711-2835064')
    sungCheck('010520-1835064')

    birthd('011230-3835064')
    birthd('010711-2835064')
    birthd('010520-1835064')

    ageCheck(1999)
    ageCheck(2001)
    ageCheck(2003)


def main():
    sungCheck(jumin)
    birthd(jumin)
    infoPrint()

main()

birthday = int(input("년  year>>> "))
ageCheck(birthday)

print()


