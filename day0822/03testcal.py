#03testcal.py

#변수선언 및 초기화
a,b = 7,2
hap,sub,gob,mok,nmg = 0,0,0,0,0 #산술 연산
x,y,z = False,False,False # 0 초기화보다는 False 권장

hap = a + b
print(a + b)
print(hap)
print('-' * 50)

x = (a > b)
print(a > b) #결과값 상상
print(x)

# 관계연산 > < >= <=  == !=
y = (a==b) 
z = (a!=b)
print(y) #False
print(z) #True

# 컴퓨터 언어 language 연산에서 산술,관계,논리 and or not in is
print()