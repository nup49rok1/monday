# 07testkorand.py

#선언 = declare
kor, eng , hap = 0,0,0  
avg = 0.0
message = '안내문' 

#처리 

kor = 65
eng = 50
hap = kor + eng
avg = hap//2

#if 조건 and 평균 70점부터, 각 과목 60점부터 합격(논리 연산자 적용)
#if 조건 or  평균 70점부터, 각 과목 60점부터 합격(논리 연산자 적용)

'''
if avg >= 70 :
    message = '축합격'
else :
    message = '재시험'
'''
if (avg >= 70 or kor >= 60 or eng >= 60) : #조건식이 복잡하면 (  )로 묶음
    message = '축합격'
else :
    message = '재시험'

# 출력
print('07testkor.py 문서 데이터 출력')
print('국어 ',kor)
print('영어 ',eng)
print('합계 ',hap)
print('평균 ',avg)
print('결과',message)

