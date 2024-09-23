#12dict.py

mysite = dict()


#데이터 저장
mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['naver'] = 'www.naver.com' #네이버로 변경
#추가
#mysite['kakao'] = 'www.daum.kr'

#키값 동일 값만 변경이 된 상태->기존의 값이 지워지면서 저장
# =>수정의 역할


#for 반복문=>3개의 결과값이 다 같은 
#제일 많이 사용하는것 같음.
#반복문 대신에 

print(mysite)
#{'insta': 'www.insta.com', 'kakao': 'www.daum.kr', 'ibm': 'www.ibm.com'}
# for key in mysite:
#     print(key,':',mysite[key])

print()
print(mysite.keys())#키값만 나욤 dict_keys(['insta', 'kakao', 'ibm'])
print() 

print(mysite.values())#value값 목록이 출력이 된다.
print()
print(mysite['kakao']) #value값 출력이 된다.

#dict_values(['www.insta.com', 'www.daum.kr', 'www.ibm.com'])
'''
insta : www.insta.com
kakao : www.daum.kr  =>에러발생X 
ibm : www.ibm.com
'''