# 01testif.py
# writer: 홍길동
'''
 if 조건:
   만족 문장기술 

 if 조건:
   만족 문장기술 ok success
 else:
   불만족 문장기술 failed
'''
#선언 = declare
kor, eng , hap = 0,0,0  
avg = 0.0
message = '안내문' 

#처리 연산, if 반복

kor = 40
eng = 85
hap = kor + eng
avg = hap/2

#문제해결 1) 평균 70점부터 축합격, 0~69 재시험
if avg >= 70 :
    message = '축합격'
else :
    message = '재시험'

# 출력
print('국어 ',kor)
print('영어 ',eng)
print('합계 ',hap)
print('평균 ',avg)
# 추가
print('결과',message)
print(' 🎁 ' *30) #윈도우키 누르면서 . 입력해서 입력받음
print()
