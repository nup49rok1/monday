#12gugudan.py문서 함수

import time
def gugudan(name,dan):
    #dan = 7
    print('저자는 ',name)
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {k*dan}')
        time.sleep(0.3)

mydata = 0 #초기값을 설정
try:
    mydata = int(input('단입력>>'))
except:
    print('정수 숫자를 입력하세요(1~9 사이를 숫자를 입력하세요)\n')

gugudan('길동',mydata) 
print()

'''
단입력>>뮤  =>잘못 입력한 경우
정수 숫자를 입력하세요(1~9 사이를 숫자를 입력하세요)
0 * 1 = 0
0 * 2 = 0
0 * 3 = 0
0 * 4 = 0
0 * 5 = 0
0 * 6 = 0
0 * 7 = 0
0 * 8 = 0
0 * 9 = 0
'''