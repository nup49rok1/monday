#03testprint.py

# 변수 하나씩 선언, 다중선언

# a=7
# b=4
# ret=0 #결과값 저장(result 축약한 변수 이름)
# 변수의 값을 다양한 형태로 출력 실습

a,b,ret=7,4,0

ret=a*b
print(ret)#7*4=28
#print('7*4=28')#이것은 계산결과값이 아닌 문자임

#print(변수,'문자',~) 나열식
print(a,'*',b,'=',ret)#중간에 연결자를 추가한 경우

#print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
print('%d * %d = %d' %(a,b,ret))

#print('{}*{}={}'.format(a,b,ret))
print('{} * {} = {}'.format(a,b,ret))

#print(f'{변수및 값}')  #format으로 실정한 경우 ->앞에 f
print('{a} * {b} = {ret}')#앞의 f와 뒤의 출력양식 사이에 공백X
print(f'{a} * {b} = {ret}')

print()