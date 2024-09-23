#01deflist.py
#TypeError: data_hap() takes 0 positional arguments but 2 were given
def data_hap(x,y,z,a,b,c):
    #숫자합계 구해서 리턴 처리
    #hap = 0   생략가능함
    hap = x + y + z + a + b + c
    return hap

def my_hap(*args): # *매개변수명 =>주소를 받을 수 있는 매개변수 
    print('args타입',type(args)) #args타입 <class 'tuple'>
    hap = 0 #생략하면 에러발생 ->누적하는 변수의 경우는 반드시 초기화 O
    #UnboundLocalError: cannot access local variable 'hap' where it is not associated with a value
    for num in args:
        hap = hap + num
    return hap

data = my_hap(6,11,3.,7,5,21,9) #실수는 허용
#data = my_hap(6,11,24,7,5,21,9)
print('데이터 결과 ',data)
print('데이터 결과 ',my_hap(6,11,3,7,5,21,9))
#print('데이터 결과 ',my_hap(6,11,'A',7,5,21,9))
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#문자는 다른 데이터이기에 에러유발 됨
print()
print('- '*50)

total = data_hap(6,11,3,7,5,21) #실수는 허용
#data = my_hap(6,11,24,7,5,21,9)
print('계산처리 합계 ',data)
print('계산처리 합계 ',data_hap(6,11,3,7,5,21))

'''
args타입 <class 'tuple'>
데이터 결과  83
args타입 <class 'tuple'>
데이터 결과  83
'''
#total = data_hap(6,9,21,7,3,21)

# print('계산처리 합계 ', total)
# print('계산처리 합계 ', data_hap(6,9,21,7,3,21))
# print()

