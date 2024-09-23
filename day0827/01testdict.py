# 01test.py

mylist = [ ] #리스트 선언
mydict = {}  #dict 선언

mydict[500] = '차박'
mydict[700] = '등산'
mydict[300] = '여행' # 나중에 새로 추가 =>키보드를 통해서 값을 넣기

#print(mydict) # 비권장 {500: '차박', 700: '등산'}

for k,v in mydict.items() :
    print(k,':',v)

'''
500 : 차박
700 : 등산
300 : 여행
'''
print()

for i,k in enumerate(mydict):
    print((i+1),'',k,mydict[k]) #enumerate 데이터 출력시 번호매기면서 출력
'''
0  500 차박
1  700 등산
2  300 여행
'''