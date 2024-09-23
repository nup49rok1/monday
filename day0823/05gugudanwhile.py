#05gugudanwhile.py

# p100 페이지 응용 문제

import time

#dan = 3
data = input('원하는 단입력>>') 
dan = int(data)
                              
k = 1
while True:
    print(f'{dan}*{k}={dan*k}') 
    k = k + 1
    time.sleep(0.5)
    if k > 9:
        break

print()

