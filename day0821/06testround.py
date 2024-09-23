#06testround.py
#변수 다중 선언

a,b,ret=9,4,0
mok=34.5637
print(mok)
#print('%d'%(mok))# 실수이지만 정수 34 출력
print('%f'%(mok)) #%f는 자릿수 지정안하면 6자릿수까지 출력
print('%.2f'%(mok)) #%f는 자릿수 지정(전체 6자리중 소수점 2자리)
print(round(mok,2)) # 내장함수 round(값,2)

#내장함수 
# print(),int(),type(),input('안내문'),str(),sum()
# round(데이터,실수자릿수2)

#%자릿수d정수 %자릿수f실수
# #print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
# print('%d*%d=%d' %(a,b,ret))

# # 전체 블록 선택후 =>ctrl+/ 전체 주석
# ret=a*b
# print(ret)#7*4=28
# #print('7*4=28')#이것은 계산결과값이 아닌 문자임

# #print(변수,'문자',~) 나열식
# print(a,'*',b,'=',ret)#중간에 연결자를 추가한 경우

# #print('%d정수 %s문자열 %f실수 %c문자' %(데이터))
# print('%d*%d=%d' %(a,b,ret))

# #print('{}*{}={}'.format(a,b,ret))
# print('{}*{}={}'.format(a,b,ret))

# #print(f'{변수및 값}')  #format으로 실정한 경우 ->앞에 f
# print(f'{a}*{b}={ret}')#앞의 f와 뒤의 출력양식 사이에 공백X

# print()