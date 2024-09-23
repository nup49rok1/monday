#homeworklotto.py

import random

# 로또 1~45 사이 숫자
# 로또 정수
# 반복문 for ,while,if
# 난수발생 6개 숫자 중복 체크
# 난수 발생후 출력은 sort 정렬해야 한다.
# set 이용하지 마세요
# 리스트이름[2] = 39

lotto = [] #데이터 담을 리스트 생성

while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :#for k in range(6)
        if (lotto.count(lotto[k]) > 1) :#특정값의 갯수가 1개이상 이라면 중복됐다면
            lotto.pop() #삭제
            lotto.append(random.randint(1,45))#추가

print(lotto)
lotto.sort()
print(lotto)

print()
print()

'''
[14, 31, 37, 7, 36, 6]
[6, 7, 14, 31, 36, 37]


PS C:\Mnet\workPython> & C:/Users/user/anaconda3/envs/ck/python.exe c:/Mnet/workPython/day0826/homeworklottoteacher.py
[3, 34, 30, 25, 36, 26]
[3, 25, 26, 30, 34, 36]


'''