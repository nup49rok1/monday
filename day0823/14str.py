# 14str.py

score = 23901
mypoint = 74
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(score +'점수') 슷자+문자=>지원x (에러유발 )

print(score ,'점수') #나열하면 에러 안나옴
print(score+mypoint) #더하기 연산 2374
print(str(score)+str(mypoint)) #230074 문자의 결합
print()
'''
2300 점수
2374
230074

'''