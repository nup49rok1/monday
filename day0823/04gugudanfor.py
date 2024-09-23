#04gugudanfor.py


import time

#dan = 3
dan = int(input('원하는 단입력>>')) #input('안내문') 문자형으로 인식
                                   #숫자로 변환해 줘야 된다.
for k in range(1,10,1) :
    #print(dan,'*',k,'=',(dan*k)) #문자를 숫자만큼 반복하게 된다.
    print(f'{dan}*{k}={dan*k}') #앞의 f를 빼면 액면그대로의 문자열 출력됨.
    time.sleep(0.5) #1초 실행속도 정지 1초 간격으로  초단위 기술

print()

#while구문에서 많이 사용 (0.5 or 1초 단위로 쓰는 것이 좋다.)
print('카카오')
print('네이버')

# 잘못 입력했을 경우의 예외처리는 다음주에 8장
# ValueError: invalid literal for int() with base 10: '3.4'
# ValueError: invalid literal for int() with base 10: 'aa'
'''
원하는 단입력>>5
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45

카카오
네이버
'''