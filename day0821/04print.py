#04testprint.py

a,b,ret=9,4,0
msg=1234

ret=a*b

print('|{}|*|{}|=|{}|'.format(a,b,ret))
print('|{}|'.format(msg)) #}{ } 안쪽이 아닌 바깥쪽에 쓰는 경우있음
# 0이 10개인 경우
print('|{:0>10,}|'.format(msg)) #> 오른쪽 맞춤,관계연산자 아님
#|000001,234|
print('|{:*>10,}|'.format(msg)) #별이 10개
#|*****1,234|
print('|{:,}|'.format(msg)) #액면 그대로 출력  1,234


""" 
 여러줄 주석  ''' ''' 이 좀더 편하다.
print(a,'*',b,'=',ret)

#print('%d정수  %(데이터))
print('%d*%d=%d' %(a,b,ret))

#print(f'{변수및 값}')  
print(f'{a}*{b}={ret}')

"""

print()