#02deflist.py
#TypeError: data_hap() takes 0 positional arguments but 2 were given


def my_hap(*args): #여러개을 받는데 같은 타입
    hap = 0 
    for num in args:
        hap = hap + num
    return hap

# data = my_hap(6,11,3.,7,5,21,9) #실수는 허용
# #data = my_hap(6,11,24,7,5,21,9)
# print('데이터 결과 ',data)
# print('데이터 결과 ',my_hap(6,11,3,7,5,21,9))

mylist = [ 6,11,24,7] #수정 O,쉽게 데이터 추가
mytuple = (5,10,23,6) #수정 X 
mylist[1] = 54
print(mylist) #[6, 54, 24, 7]

mytuple[1] = 94 #에러 수정
#TypeError: 'tuple' object does not support item assignment
print(mytuple)