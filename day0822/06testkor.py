# 06testkor.py

'''
 if 조건:
   만족 문장기술 

   
 if 조건:
   만족 문장기술 ok success
 else:
   불만족 문장기술 failed

if 조건:  
   조건1 만족 문장기술
 elif 조건2 :
    조건2 만족 문장기술
 elif 조건3 :
    조건3 만족 문장기술
 else:
   불만족 문장기술

   100 ~90  A
   89 ~80  B
   79 ~70  C
   69 ~60  D
   59 ~0  F
'''
#선언 = declare
kor, eng , hap = 0,0,0  
avg = 0.0
message = '안내문' 
#추가
grade = 'F'

#처리 연산, if 반복

kor = 90
eng = 96
hap = kor + eng
avg = hap//2 #hap/2 ->정수형으로 출력

#문제해결 1) 평균 70점부터 축합격, 0~69 재시험
if avg >= 70 :
    message = '축합격'
else :
    message = '재시험'

#잘못된 처리) 
# 평균 100~90 A, 89~80 B ,79~70 C ,69~60 D , 59~0 F
# 세번째까지는 각자 따로 실행 =>조심할것.
if avg >= 90 :
    grade = 'A'

if avg >= 80 :
    grade = 'B'

if avg >= 70 :
    grade = 'C'

# 4번째는 하나로 취급
if avg >= 60 :
    grade = 'D'
else:
    grade = 'F'

#문법에러, 처리버그=에러
# 출력
print('국어 ',kor)
print('영어 ',eng)
print('합계 ',hap)
print('평균 ',avg)
# 추가
print('학점',grade)
print('결과',message)
print(' 🎁 ' *30) #윈도우키 누르면서 . 입력해서 입력받음
print()
