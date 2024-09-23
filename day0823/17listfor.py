#16list.py

mylist = ['tea',7]  
print(mylist)

mylist.append('파이썬')
print(mylist)

mylist.append(23)
print(mylist)

mylist.insert(1,'blue')
print(mylist)
print('- ' * 50)
# for a in mylist:
#     print(a,end=' ') #한줄에 다 출력

# ['tea', 'blue', 7, '파이썬', 23]
# 수정할때
mylist[0] = 'kakao'
mylist[2] = 94
print(mylist) 
# 최종 결과 ['kakao', 'blue', 94, '파이썬', 23]


# 삭제 blue삭제 del mylist[1], remove pop(위치)
# 정답 mylist.pop(1) 권장

del  mylist[1]
print(mylist) #['kakao', 94, '파이썬', 23]

#mylist.sort() #TypeError: '<' not supported between instances of 'int' and 'str'
#주의 사항 sort() 적용은 같은 타입만 가능

print()
'''
['tea', 7]
['tea', 7, '파이썬']
['tea', 7, '파이썬', 23]
['tea', 'blue', 7, '파이썬', 23]
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -       
['kakao', 'blue', 94, '파이썬', 23]
['kakao', 94, '파이썬', 23]

#콘솔에서 빠져나가는 방법 ctrl+z  or exit()를 입력하면 된다.
'''

