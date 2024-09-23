#09testfor.py

# 문자열,list,tuple,set,dict
# 반복데이터 사용

'''
 for 변수대표 k in range(10) :
      10회저리 0~9까지 10회처리

 for 변수대표 k in range(1,10) :
      9회저리 1~9까지 9회처리

 for 변수대표 k in range(1,10,1) :
      9회저리 1~9까지 9회처리 
      1씩증가일때 3번째 1생략  

 while 조건:
    조건만족시 루프 loop 처리
    무한루프처리일때 if제어문으로 break 반복탈출  
'''

#for,while 연습할때 사용 a,b,hap,tot
a,b=0,0
hap,tot=0,0

#첫번째 a, hap 1~5 출력 누적

'''
  1  1
  2  3
  3  6
  4  10
  5  15
'''
a = a+1; hap=hap+a; print(a, hap) #문장따로 ; 로 구분(한라인에서)
a = a+1; hap=hap+a; print(a, hap)
a = a+1; hap=hap+a; print(a, hap)
a = a+1; hap=hap+a; print(a, hap)
a = a+1; hap=hap+a; print(a, hap)
print()

#변수 재사용할때 초기화 점심식사후
#for반복문, 대입연산

a , hap = 0,0 # 재선언보다는 초기화
for k in range(5):
    a = a + 1
    hap = hap + a
    print(a,hap)
'''
6 21
7 28
8 36
9 45
10 55

'''

print()
