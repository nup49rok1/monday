#변수 선언부분 = 변수 데이터 초기화 =declare
#변수 초기화=기본값  대입 =할당
#변수 이름 명명  첫글자는 소문자로 시작(첫글자 숫자 비권장,특수문장 비권장)
#변수 이름 명명 첫글자  소문자 eng, my_eng,myeng,my-avg, team_kor,

title='데이터 점수'
name='길동'

kor=90
eng=85
hap=0  #hap,total,grandTotal    sum 키워드 금지 sum() 내장함수 있어서 
avg=0.0 #avg 평균 myage 권장 

# 로직=처리 담당 연산(산술,관계,논리),연산결과 조건(if, 반복문(for,while)
# hap=(kor+eng)
# avg=(kor+eng)/2
#ctrl+/ 주석

#로직 =연산 처리
hap=kor+eng #사칙연산 +,-,*,/ 몫 % 나머지
avg=hap/2

#처릭ㄹ과 출력 print('안내문',데이터)
#print() 내장함수는 라인개행포함  <br> 역할

print('이름=',name)
print('국어=',kor)
print('영어=',eng)
print('총점=',hap)
print('평균=',avg)
print()