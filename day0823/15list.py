#15list.py
import time

#리스트 목록 list() 반복 O, 순서 O
 
mylist = ['kim',78,3.1415,True,'F',"kim",78]  #list()
print(mylist)
print()
time.sleep(1)

#set() 반복X, 순서X
myset = {'red',78,23,'red',78,'red'} 
print(myset)
time.sleep(1)

#tuple 튜플, tuple(),수정 불가 
mytuple = ('blue',21,'A')  
print(mytuple)
print()
time.sleep(1)

#dict 딕트 dict() key|value 700:'구글'
mydict = {100:'naver',200:'kakao' } #dict()
print(mydict)
print()

'''
['kim', 78, 3.1415, True, 'F', 'kim', 78]

{'red', 78, 23}
('blue', 21, 'A')

{100: 'naver', 200: 'kakao'}
'''