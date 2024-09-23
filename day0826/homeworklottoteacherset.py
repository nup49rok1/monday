#04lotto.py

import random

# 로또 1~45 사이 숫자
# 숫자 중복체크
# 리스트대신에 set 사용

lotto = [ ] #데이터 담을 리스트 생성

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

''' 나중에 리스트 대신에 set타입으로 변환 '''

myset = {7,12,29,45,3,36,12}
print(myset) # {29, 3, 36, 7, 12, 45}