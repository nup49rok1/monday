#homeworksu.py

#list [] 사용금지
#while 반복문 사용 =>숫자를 거꾸로 출력 2495
#print(),if

# mylist = [ 5,9,4,2]
# print(mylist)

# mylist.reverse()
# print(mylist)


su = 5942
print(su)
while True:
    print(su % 10,end='')#먼저 10으로 나눌때의 나머지 2가 출력
    #print(su % 10,end= '')
    su //=10 #// 나눗셈 연산의 결과를 정수형으로 변환시키주는 연산자
    if su == 0 :
        break

'''
입력받은값 5492 =>처음은 10으로 나눌때의 나머지 구함 549.2=>2
                 54.92 =>두번째 9
                 5.492 =>세번째 4
                 0.5492 =>네번째 5
 
'''
sj = {'kim':90, 'lee':70 }
'''
[5, 9, 4, 2]
[2, 4, 9, 5]
PS C:\Mnet\wo
'''