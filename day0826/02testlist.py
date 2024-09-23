#02testlist.py

data = [  #4행 * ?열
         
        #  [1,2,3,4], #열의 갯수가 맞지않으면 에러가 발생이 된다.
        #  [5,6,7,8],
        #  [9,10,11,12]
        [71,72,73,74,70],
        [25,26,28],
        [39,10,11,12],
        [33,55]

       ]
for k in range(len(data)) :#3행을 가리킴 열갯수 고정임
    for b in range(len(data[k])) :#각행의 열의 갯수만큼 뽑아와서 k(열의 갯수)
        print(data[k][b],end =' \t') #행,열 출력
    print()#줄바꿈

print()  
'''
71      72      73      74      70 
25      26      28 
39      10      11      12 
'''

# 힌트 중첩 for반복문 권장, while 반복문 비권장
# range(len()) 이용하면 편리

# for a in range(0,3,1) :#3행을 가리킴 열갯수 고정임
#     for b in range(0,4,1) :
#         print(data[a][b],end =' \t') #행,열 출력
#     print()#줄바꿈

print()

'''
1 2 3 4
5 6 7 8
9 10 11 12
'''

