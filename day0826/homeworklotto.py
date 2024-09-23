#0homeworklotto.py

import random

# 로또 1~45 사이 숫자
# 로또 정수
# 반복문 for ,while,if
# 난수발생 6개 숫자 중복 체크
# 난수 발생후 출력은 sort 정렬해야 한다.
# set 이용하지 마세요

alist = [] #데이터 담을 리스트 생성

for k in range(6) :
    com = random.randint(1,45) #1~45 사이의 임의의 수 출력
    #alist.append(com)
#print(alist) 중복된 값이 나올 수도 있다.
    #추가
    while com in alist: #중복된 데이터가 들어 있다면 
        com = random.randint(1,45) #다시 난수발생시킴
    alist.append(com)
    alist.sort()
    #print(com,end = '\t')
print(alist)
print()
print()
'''
on/day0826/homeworklotto.py
[2, 3, 26, 39, 44, 45]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0826/homeworklotto.py
[1, 9, 11, 13, 18, 28]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0826/homeworklotto.py
[1, 3, 8, 11, 19, 37]

'''