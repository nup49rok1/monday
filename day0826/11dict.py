#11dict.py

mysite = dict()


#데이터 저장
mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['ibm'] = 'www.ibm.com'


#for 반복문=>3개의 결과값이 다 같은 
#제일 많이 사용하는것 같음.
for key in mysite:
    print(key,':',mysite[key])

print()
print()

for i,k in enumerate(mysite) :
    print(i,k,':',mysite[k])

print()
print()

'''
insta : www.insta.com
kakao : www.kakao.net
ibm : www.ibm.com


0 : www.insta.com
1 : www.kakao.net
2 : www.ibm.com
'''

for k,v in mysite.items() :
    print(k,':',v)


# dict=딕트 k:v
'''
insta : www.insta.com
kakao : www.kakao.net
ibm : www.ibm.com


0 : www.insta.com
1 : www.kakao.net
2 : www.ibm.com


insta : www.insta.com
kakao : www.kakao.net
ibm : www.ibm.com
'''