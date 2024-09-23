# 15for.py

# for 반복문 대표변수 사용 range(시,최,증감)
# 10,9,8,7,6,5,4,3,2,1

for k in range(1,11) :
    print(k)

print()

for k in range(10,1,-1) : #10을 시작, 종료값 1 감소값 -1
    print(k)

print()

for k in reversed(range(1,11)) : #reversed함수를 이용
    print(k)

'''
1
2
3
4
5
6
7
8
9
10

10
9
8
7
6
5
4
3
2

10
9
8
7
6
5
4
3
2
1
PS C:\Mnet\workPython>
'''