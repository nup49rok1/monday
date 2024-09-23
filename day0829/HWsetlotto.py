#HWsetlotto.py

# 추천 lotto = set() #셋 항목함수 lotto.add()
# 금지 lotto = list()  리스트추가 append()
# 난수 로또숫자 발생,중복체크, set 추가
# set 데이터타입을 list 변환
# 출력은 오름차순 적용 sort()

import random

def mysetlotto():
    print()
    lotto = set()
    # while ~ while ~ if ~ else
    # while ~ for ~if ~ else
    # while ~ i ~ else
    for k in range(6):
        com = random.randint(1,45)
        #print(com, end =' ')
        if com not in lotto:
            lotto.add(com)
    
    for i in sorted(lotto):
         print(i,end =' ')
    
def main():
    mysetlotto()


main()