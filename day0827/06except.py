#06except.py
# try: ~~ except: ~~ 


# 변수선언, 값대입 선언부분 declare
x ,y = 7,0
hap , gob, mok, nmg = 0,0,0,0

# 예외 처리 연산처리, if 제어처리, 반복처리
try:
    pass # 당장 쓸코드가 없을시 써주면 에러가 안나옴(안전 장치)
    hap = x + y
    mok = x / y #실행중 연산처리 에러발생 7/0 24
    # ZeroDivisionError: division by zero
    #에러발생하면 except 영역으로 이동한다.(다음문장 수행X)
    #에러나오면 아래문장은 실행이 되지를 않는다.
    gob = x * y
    nmg = x % y
    print(f'{x} + {y} = {hap}')
    print(f'{x} / {y} = {mok}')
    print(f'{x} % {y} = {nmg}')
    print(f'{x} * {y} = {gob}')

except:
    pass
    print('주의 경고!!! 연산처리가 잘못 되었습니다.')

# 에러발생시 처리되는데 초기값으로 설정해서 출력이 된다.(0인 경우)
# print(f'{x} + {y} = {hap}')
# print(f'{x} / {y} = {mok}')
# print(f'{x} % {y} = {nmg}')
# print(f'{x} * {y} = {gob}')
print()
print('쇼핑목록')
print('주차처리')
print('정산성공')

'''
7 + 5 = 12
7 / 5 = 1.4
7 % 5 = 2
7 * 5 = 35
'''
'''
주의 경고!!! 연산처리가 잘못 되었습니다.
  except 밑에 쓰는 경우
7 + 0 = 7
7 / 0 = 0
7 % 0 = 0
7 * 0 = 0

쇼핑목록
주차처리
정산성공
'''




