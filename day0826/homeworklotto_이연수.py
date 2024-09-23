#homeworklotto2.py

import random

# 로또 1~45 사이 숫자
# 로또 정수
# 반복문 for ,while,if
# 난수발생 6개 숫자 중복 체크
# 난수 발생후 출력은 sort 정렬해야 한다.
# set 이용하지 마세요

lotto = [] #데이터 담을 리스트 생성

for k in range(6) :
    com = random.randint(1,45) #1~45 사이의 임의의 수 출력
    if com not in lotto:#중복되지 않았으면 리스트에 데이터를 추가
        lotto.append(com)
    lotto.sort()
    
print(lotto)
print()
print()
'''
[2, 5, 6, 15, 22, 41]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe "c:/Mnet/workPython/day0826/homeworklotto copy.py"
[7, 10, 13, 27, 33, 41]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe "c:/Mnet/workPython/day0826/homeworklotto copy.py"
[20, 27, 33, 36, 42]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe "c:/Mnet/workPython/day0826/homeworklotto copy.py"
[8, 27, 31, 32, 43]

'''