#02split.py

url = 'www.google.com'
print(url)

myret = url.split('.')# . 으로 분리 =>자동으로 리스트화 된다.
print(myret) #리스트 ['www', 'google', 'com']
print(url.split(','))  #['www.google.com'] .이 없으면 한덩어리로 분리
print(list(url))#['w', 'w', 'w', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
# 리스트화 시키면 하나하나씩 분리가 된다.
'''
www.google.com
['www', 'google', 'com']
['www.google.com']
['w', 'w', 'w', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
'''
print()