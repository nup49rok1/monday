#01string.py

# str(),len()  내장함수

x = 'blue'
y = 1234
#print(x + y) #TypeError: can only concatenate str (not "int") to str
#타입이 맞지않아서 에러 발생(문자+숫자)

print( x + str(y)) #숫자->문자로 변환
print( x,y) #분리  문자는 문자대로, 숫자는 숫자대로 ,로 나열한 경우(공백 포함)

'''
blue1234
blue 1234
'''
print(f'{x}{y}') #분리 문자,숫자 =>공백표시 안됨
print(x,y) #분리사이 공백표시 문자,숫자
'''
blue1234
blue 1234
blue1234
blue 1234
'''
print('- '*50)

msg = 'sakbtb'
print('길이',len(msg))
print('갯수',msg.count('b')) #반복되는 문자의 갯수를 알고자 할때 사용
'''
길이 6
갯수 2
'''
#kb 글자 단어를 추출하고 싶다. [시:끝+1]
my = msg[2:4] #리턴값을 받는 경우
print(my)
print(msg[2:4]) #kb

print()
'''
kb
kb
'''