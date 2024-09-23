#04lotto.py

import random

# 로또 1~45 사이 숫자
# 로또 정수
# 반복문 for ,while
# 난수발생 6개 숫자 중복 체크
# 난수 발생후 출력은 sort 정렬해야 한다.
# 24      24      1       36      7       28 (중복문제해결)

for k in range(6) :
    com = random.randint(1,45) #1~45 사이의 임의의 수 출력
    print(com,end = '\t')

print()
print()