# 04delpop.py
import time  #시간차를 두고 실행되고 싶다.

data = [7,8,9,10,3,5,2,4,1]

data.remove(9) #9삭제
data.pop() #2 삭제
print(data) #[7, 8, 10, 3, 5, 2, 4]

#del data[10] #IndexError: list assignment index out of range (위치)
del data[2]
print(data) #[7, 8, 3, 5, 2, 4]
time.sleep(1) #1초후 실행하라

#문제 8,3,5,2 4개를 삭제하고 싶다.
del data[1:5] #슬라이싱 문자열 [시작:끝+1]
print(data) #[7, 4]

time.sleep(0.5)
data = [7,8,9,10,3,5,2,4,1] #문제 모든 데이터 전부 삭제
#data.clear() #clear 삭제가 안되고 적용안됨=>clear()이 정답임.
# count(), len()  조심할것.
# count(인자),len(데이터적용대상자(리스트/딕트/문자열)) 
# 가 있어야 한다. 함수사용시 주의할것.
del data[:]  # 전체삭제 비권장
print(data)# []
print('삭제 연습끝 드뎌 dict 실습 k:v')


# remove,del,pop,clear 제거 삭제 기능
# remove(데이터값)
# pop(위치) ,pop() 맨끝(매개변수 없는 경우)
# del 대상[위치]
# clear 전부 삭제

# 추가 append(), insert(위치,값), add()
# 추가 딕트이름[k300] = dataValue
# 덮어쓰면서 추가된다. 딕트이름[k300] = dataValue

print()