#13dict.py

mysite = dict()


#데이터 저장
mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['naver'] = 'www.naver.com' #네이버로 변경
#추가
mysite['google'] = 'www.google.org'

print(mysite['kakao'])
print(mysite.get('kakao')) #get이 훨씬 더 많이 사용한다
print()

#위의 둘의 결과는 동일하다.

# 에러 발생 print(mysite['kaka']) #키값을 잘못 기술
print(mysite.get('kaka')) #키값을 잘못 기술
#=>get()함수는 키값이 없으면 None
print()

'''
www.kakao.net
www.kakao.net

None
'''

#데이터가 있는지 없는지 체크(key값 체크)
#키값 있어야 딕트이름[키값] 출력 및 수정,신규등록이 가능
mya = 'naver' in mysite #키값(문자열)
myb = 'navr' in mysite

print(mya) #True
print(myb) #False