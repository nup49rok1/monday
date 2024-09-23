#12list.py

import time

lista = [2,1,9,5,3,7,6 ]
print(lista) 

time.sleep(1)
print()

#  9 5 3 데이터 추출
time.sleep(1)
print(lista[2:4]) #[9,5]
print(lista[2:5]) #[9, 5, 3] 0

time.sleep(1)
print(lista[-2])#7
print(lista[5])#7

time.sleep(1)
print(lista[3:])#[5, 3, 7, 6]

'''
[2, 1, 9, 5, 3, 7, 6]

[9, 5]
[9, 5, 3]
7
7
[5, 3, 7, 6]
'''