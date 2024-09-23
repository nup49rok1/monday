# 숙제 homeworkcal.py

a,b=9,5

hap,sub,gob,nmg=0,0,0,0
mok=0.0

hap=a+b
sub=a-b
gob=a*b
mok=a/b
nmg=a%b

# print()  % {} f{} ) 다양한 출력
print(a,'+',b,'=',hap)

#print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
print('%d - %d = %d' %(a,b,sub))

print('{} * {} = {}'.format(a,b,gob))

#print(f'{변수및 값}')  #format으로 실정한 경우 ->앞에 f
print(f'{a} / {b} = {mok}')#앞의 f와 뒤의 출력양식 사이에 공백X

print(a,'%',b,'=',nmg)

'''
 9+5=14
 9-5=4
 9*5=45
 9/5=1
 9%5=4
'''