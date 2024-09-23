# homework2if.py

su = 6
# 정수 = int = integer

# 문제해결 su 데이터값 짝수,홀수
# if~~else

mok = su % 2 #몫(/)이 아니라 나머지(%)로 구해야 한다.
if mok == 0:
    print(su,'값은 짝수입니다.')
else:
    print(su,'값은 홀수입니다..')

print('-'*50)


if su %2 == 0:
    print(su,'값은 짝수입니다.')
else:
    print(su,'값은 홀수입니다..')

print('-'*70)

if su %2 != 0:
    print(su,'값은 홀수입니다.')
else:
    print(su,'값은 짝수입니다..')
    
print('-'*70)
