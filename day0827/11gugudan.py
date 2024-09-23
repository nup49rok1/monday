#gugudan.py문서 함수


# 내장함수
# list(),len(),tuple(),set()
# str(),int(),round(),print(),input()

# 리턴값X ,매개인자 X  일반함수
def book():
    # 서점,예약,내용 위주
    pass

def main():
    # 메인함수 진입시작
    pass

import time
def gugudan(dan):
    #dan = 7
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {k*dan}')
        time.sleep(0.3)

def mysum(a,b):
    print(a,b,'합계=',(a+b))

gugudan(21) #함수이름(21 매개인자=argument=parameter)
print('구구단 연습 4:37')
print()

#문제 mysum함수 호출
mysum(17,26)

# 파이썬 함수 def 함수이름() :
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값
# 함수는 호출 call 