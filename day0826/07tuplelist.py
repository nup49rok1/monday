#07tuplelist.py

# 튜플 ( ) 표식
# 튜플은 리스트 비슷, 중복허용,수정불가
pos = ('홍대',126.723, 37.081,'홍대',290.345,126.159)

# 튜플 for반복문으로 출력
for k in range(len(pos)) :
    print(pos[k],end = '\t')

print()
print('- ' * 30)
print()
'''
홍대    126.723 37.081  홍대    290.345 126.159
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
'''
#enumerate(나열)->인자를 2개 줘야 된다.
'''
순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 인덱스와 값을 포함하여 리턴
for문과 함께 자주 사용됨
인덱스와 값을 동시에 접근하면서 루프를 돌리고 싶을 때 사용
'''
for i,v in enumerate(pos): #key,value값으로 출력
    print(i, ':', v)

'''
0 : 홍대
1 : 126.723
2 : 37.081
3 : 홍대
4 : 290.345
5 : 126.159  
'''
#(i+1) =>1,2,3으로 출력
for i,v in enumerate(pos): #key,value값으로 출력
    print((i+1),':',v) #몇번째 항목인지 출력하고자 할때 enumerate() 함수 사용