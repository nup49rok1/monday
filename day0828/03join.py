#03Join.py

url = 'www.google.com'
print(url)

#연결
ct = ' ' #공백도 하나의 문자열로 취급
print(ct.join(url))

print()
'''
www.google.com
www.google.com  =공백이 없는 경우

www.google.com
w w w . g o o g l e . c o m  =>공백이 있는 경우 없으면 위의 글자와 동일하다.
'''