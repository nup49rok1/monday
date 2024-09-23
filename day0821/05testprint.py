#05testprint.py

# 자리수를 정해서 출력


msg=97234

print('{}'.format(msg)) # 정석  97234
print('{:>10,}'.format(msg)) #총 10자릿수 > 오른쪽맞춤
print('{:<10,}'.format(msg)) #총 10자릿수 < 왼쪽맞춤
print('{:^10,}'.format(msg))  #총 10자릿수 ^ 중앙맞춤

print('-'*100) #-문자열 100번 반복
print('{:0>10,}'.format(msg)) ##000001,234
print('{:*>10,}'.format(msg)) #*****1,234
print('{:,}'.format(msg)) #액면 그대로 출력  1,234

print()
'''
97234
    97,234
97,234
  97,234
----------------------------------------------------------------------------------------------------
000097,234
****97,234
97,234

'''