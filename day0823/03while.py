
#03while.py

#su = 0 NameError: name 'su' is not defined. Did you mean: 'sum'?
#연산할때 선언된 변수가 없을때 발생하는 에러

su = 0 #변수선언(declare) + 값 초기화

while True:
    #su = 0  무한루프에 빠짐 주의할것.(콘솔창에서 찍고 ctrl+c 강제입력 해줌)
    su = su + 1
    if su == 5:
        continue
    print(su,end = ' ')#한줄 출력
    '''
    if su == 5:  출력후에는 의미가 없다. 출력전에 해야 된다.
        continue
    '''
    if su == 10:
        break

#문제 1 2 3 4 6 7 8 9 10 =>5만 건너띄기 (출력X)
print()
print('-  '*30)
'''
03while.py
1 2 3 4 6 7 8 9 10 
-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
'''