#03lotto.py
# 조건1 숫자 6개
# 조건2 중복숫자 제거
# 조건3 정수숫자로만 구성 문자 X, 실수 X

lotto = [23,19,5,42,19,27,23,5,23]
myset = set(lotto) #중복데이터가 많을 경우(filtering)
                   #응모할때 하나 데이터만 유지하고 싶을때
print(myset) #{5, 42, 19, 23, 27}

lotto = list(myset)
lotto.sort()# 오름차순 a,b,c ~ 1,2,3~
print(lotto) #[5, 19, 19, 23, 27, 42]
#[5, 19, 23, 27, 42]

mylength = len(lotto) #데이터 갯수를 필요로 할때 전역함수 len()사용
if mylength < 6 :
    print('항목 하나 추가하셔야 처리가능')
elif mylength > 6 :
    print('항목 데이터 초과입니다.\n다시 확인하세요')
elif mylength == 6:
    print('데이터항목 정상입니다.')

#문제 lotto갯수 6개 아니면 추가
#len() 전역함수