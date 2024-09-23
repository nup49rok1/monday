import datetime #from import 
import time

# x = datetime.now() #에러 발생->실행시
# print(x)

jumin = '011230-3835064'


#문제1 성별체크 1/3 남자 2/4 여자
#문제2 생일 12월30일 생일 축하합니다.->고객의 정보를 확인=>쿠폰을 전달
#문제3 나이계산  2024-1997=??? 

print(jumin[7:8])

#문제1
if (jumin[7:8] == '1' or jumin[7:8] == '3'):
    print('당신은 남자입니다.')
else:
    print('당신은 여자입니다.')

print('- '*50)

def sungCheck(jumin):
    if (jumin[7:8] == '1' or jumin[7:8] == '3'):
        print('당신은 남자입니다.')
    else:
        print('당신은 여자입니다.')

sungCheck('011230-3835064')
sungCheck('0110711-2835064')
sungCheck('010520-1835064')

#문제2
print(jumin[2:4])#12
print(jumin[4:6])#30

mon=jumin[2:4]
dy=jumin[4:6]
print(f'당신의 생일은 {mon}월 {dy}일 이군요!' )

print('*'*50)

def birthd(jumin):
    mon=jumin[2:4]
    dy=jumin[4:6]
    print(f'당신의 생일은 {mon}월 {dy}일 이군요!' )

birthd('011230-3835064')
birthd('010711-2835064')
birthd('010520-1835064')


#문제3 
y = datetime.datetime.now() #정답
z = str(y)
print(int(z[0:4])-1969) #2024-출생년도 = 나이 계산
print()

print('- '*50)

#문제4  함수작성

def ageCheck(birthday):
    y = datetime.datetime.now() #정답
    z = str(y)
    print(f'당신의 나이는 {int(z[0:4])-birthday} 살입니다.') #2024-출생년도 = 나이 계산
    print()

ageCheck(1969)
ageCheck(2001)
ageCheck(2003)


print()
