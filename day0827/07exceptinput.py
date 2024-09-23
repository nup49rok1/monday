#07exceptinput.py
# 문제1 dan 입력 키보드 input(), 형변환
# 문제2 예외처리 try: ~ except:~  문자입력하거나 실수값 입력하는경우
# 문제3 dan입력범위 정수 1 이상 2~9사이 숫자만 입력
# 1건이상 처리는 무조건 반복문이 들어간다.

import time

# dan = 3
dan = 0 #초기값

try:

    dan = int(input('원하는 단을 입력>>>'))#문자->정수로 변환해야함
    #잘못된 결과 출력하기 원하지 않은 경우에는 이 부분에 써준다.
    if dan < 2 or dan > 9 :
        print('숫자범위는 2~9사이 숫자입니다.\n 다시 입력하세요')

    for k in range(1,10,1) :
        print(f'{dan} * {k} = {dan*k}')
        time.sleep(0.5)
except:
    pass

# for k in range(1,10,1) :
#     print(f'{dan} * {k} = {dan*k}')
#     time.sleep(0.5)

print()
time.sleep(0.5)
print('포인트 7점획득')
print('포인트 5점이상이면 vip자격만족대상입니다.')

print()
print('- '*50)
'''
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27

포인트 7점획득
포인트 5점이상이면 vip자격만족대상입니다.
'''