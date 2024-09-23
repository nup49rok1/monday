#11list.py

import time

lista = [2,1,4,5,3 ]
print(lista) 

#lista.sort() #[1, 2, 3, 4, 5]
# lista.sort(reverse=True)
# print(lista) #[5, 4, 3, 2, 1]
time.sleep(0.5)
lista.insert(2,9) #2번째 요소에 9을 저장(추가)
print(lista)#[2, 1, 9, 4, 5, 3]

time.sleep(1)
lista.append(7)#맨끝에 추가 append
print(lista)#[2, 1, 9, 4, 5, 3, 7]

time.sleep(1)
#lista.remove(8) #없는 부분을 삭제하는 경우(에러유발)
#ValueError: list.remove(x): x not in list
#lista.pop() # 맨 마지막거 삭제
#print(lista) #2, 1, 9, 4, 5, 3]

lista.pop(3)#3인데스번호에 해당되는 데이터 삭제
print(lista) #[2, 1, 9, 5, 3, 7]

time.sleep(1)
lista.reverse()
print(lista)#[7, 3, 5, 9, 1, 2] sort가 안된 상태의 정렬임

print()
'''
[2, 1, 4, 5, 3]
[2, 1, 9, 4, 5, 3]
[2, 1, 9, 4, 5, 3, 7]
[2, 1, 9, 5, 3, 7]
[7, 3, 5, 9, 1, 2]
'''