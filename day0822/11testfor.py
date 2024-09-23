#11testfor.py

# 변수 선언안하고 for 대표변수 처리

for k in range(1,1001,1) :
    print(k,end='\t') 
    #문제1  한줄=한행=row 5개씩 출력=>5의 배수
    if k % 5 == 0: 
        print()

    #문제2  40숫자 출력  if 조건 반복 탈출 break (탈출문)
    if k==40:
        break
print()
print()
#1   2   3   4    5
#6   7   8   9    10
#11  12  13  14   15
#16   17  18  19  20
#21   22  23  24  25
#26   27  28  29  30