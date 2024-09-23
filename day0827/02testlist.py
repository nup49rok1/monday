# 02test.py

mylist = [ ] #리스트 선언
mydict = {}  #dict 선언

mylist.append('lee') #뒤에 추가
mylist.append(90)
mylist.append(85)
mylist.append(True)
mylist.append(90)
mylist.insert(1,'빅데이터') #1번 데이터 빅데이터넣기

#문제 85 데이터 삭제 remove(), pop() del []
# mylist.remove(87) ValueError: list.remove(x): x not in list
# 데이터 없는 경우 에러 발생

mylist.remove(85) 

# print(mylist) #비권장 ['lee', 90 ~]
# print()

for k in mylist:
    print(k,end='\t')
print()
print('- '*50)
'''
lee     빅데이터        90           True
'''
#리스트 갯수 count(데이터), len()
#cnt = mylist.count(90)
#print('리스트 갯수 ',cnt) #주어진 데이터 갯수 출력
print('리스트 갯수 ',mylist.count(90)) #이렇게 해도 된다.

#예외처리 실습 ~~~ 딕트 실습

