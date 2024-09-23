#07comprehension.py  [연산 if/else  for  ]

message = ['spam','ham','spam','ham','spam','spam','spam']

#문제1 for반복 ~if 제어
#span출력,갯수출력

message_cnt = 0
for k in message :
    if k == 'spam':
        print(k,end=' ')
        #정석 message_cnt = message_cnt + 1
        message_cnt += 1 #대입 연산자

#8번 예제하고 나서 추가 코딩
print() 
print('갯수=>',message.count('spam'))
print('갯수=>',message_cnt)

'''
갯수=> 5
갯수=> 5
'''

#문제2 [맨앞 if조건 else 불뒤 for ]comprehension \ 처리
#문제2 [맨앞 for ]comprehension \ 처리
#temp_list= [ k for k  in message if k=='spam'] #for k in message :
# 형식)  [ 표현식 for 구문 if 조건식]
temp_list= [ k for k  in message ]  # for문의 데이터를 전부 출력
#temp_list= [ k for k  in message if 'spam' in k] for문의 데이터를 조건에 만족O
           #['ham','ham']
print('temp_list=',temp_list)

