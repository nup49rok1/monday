#12forif.py

#  for 대표변수 처리
# 반복 - for, while
# 반복에서 보조 제어문 break 반복탈출, continue 복귀

for k in range(1,11) :
    if k==5: 
        continue  #for문이 5가됐을 경우 for문위로 올라감
    print(k,end=' ') 
    #보조 제어 break문장 기술 if k==5: break
    #보조 제어 continue문장 기술 
    '''
    if k==5: 
        continue 뒤에 배치하면 5을 skip하지 않는다 위치가 중요하다.
    '''

'''
1 2 3 4 6 7 8 9 10
'''