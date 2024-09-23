#06forstart.py
# 피라미드 찍기(ppt에서 복사해서 출력해봄 (로직 분석해 봄))
n = 5
for i in range(n):
    #5-(0+1)=4
    for j in range(n - (i + 1)):       # 공백을 출력함
        print(' ', end = '') #4칸 공백
    for j in range(2 * i + 1):         # '★'를 출력함
        print('★', end = '')
    print()

print()
'''
06.forstar.py
    ★
   ★★★
  ★★★★★
 ★★★★★★★
★★★★★★★★★
'''