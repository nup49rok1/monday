#HWyear.py

import sys

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]


# year = int(input("년  year>>> "))
# month = int(input("월 month>>> "))
#date = int(input(" date>>> "))

#리스트 day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 리스트,튜플, 문자열 없이 입력데이터 if 제어문
# if 제어문 or/and 중첩 if

'''
  윤년기준
   1.4의 배수
   2.100의 배수가 아닌 4의 배수
   3.400의 배수
'''
# 2024 2 입력하면 윤년입니다.
# 2024년 2월 29일 / 2020년 2월 29일
# 2021  2022년  2023년 28일

def YunTest(year):
    if year % 400 == 0 : # 400의 배수라면 
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0 # 참이면 True, 거짓이면 False
    


def main():
    year = int(input("년  year>>> "))
    bool=YunTest(year)
    if bool == True:
        print(year,'은 윤년입니다.')
    else: 
        print(year,'은 윤년이 아닙니다.')
    
main()

data = '''
kim 840916-*******
lee 921207-*******
goo 981024-*******
'''