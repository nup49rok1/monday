
#02while.py

su,tot = 0,0

while True:
    su = su + 1
    tot = tot + su #tot 누적 합계를 출력 
    print(su,tot)
    if su == 10:
        break

print()
'''
1 1
2 3
3 6
4 10
5 15
6 21
7 28
8 36
9 45
10 55
'''