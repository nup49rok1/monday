#10dict.py

mysite = { }
mydata = dict()

#데이터 저장
mysite['naver'] = 'www.naver.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'

#제일 단순 주석
#print(mysite) #{'naver': 'www.naver.com', 'kakao': 'www.kakao.net'}

print(mysite['naver'])
print(mysite['kakao'])
print(mysite['ibm'])
print()
'''
www.naver.com
www.kakao.net
www.ibm.com
'''
#for 반복문

for key in mysite:
    print(key,':',mysite[key])

'''
naver : www.naver.com
kakao : www.kakao.net
ibm : www.ibm.com
'''