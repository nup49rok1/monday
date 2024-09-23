# homeworkstar.py문서

# 100페이지 while 반복문 사용 금지

# 조건 중복 for 반복문
# 처리 지역변수, 특정변수 필요없음
# 반복문 대표변수 x,y i,j, a,b

# for a in range(1,11,1) :
#     for b in rnage(1,11,1) :
#         pass

#  윈도우+. 이모지 사용
'''
샘플링 ㅁ 입력하고 한자키를 눌러서 별을 선택

★
★★
★★★
★★★★
★★★★★

★★★★★
★★★★
★★★
★★
★

'''
#0부터 시작하면 5개의 별이 출력이 된다.
for a in range(0,6,1) : #5행을 의미(=가로=row)
    for b in range(0,a,1): #열
        print('★',end='')#end옵션 주지않으면 세로로 출력
    print()

'''
for a in range(1,6,1) :
    for b in range(1,6,1) :
        if(a<=b):
            print('★',end="")
        b+=1
    print()
'''
'''
★★★★★
★★★★
★★★
★★
★
'''