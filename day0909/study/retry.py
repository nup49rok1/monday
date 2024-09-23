
num,result,i = 0, 0, 1
while True:
    num = int(input("1~10 숫자 이력:"))
    if num < 1 or num > 10:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        continue
    break
while i<=num:
    result += 1; i+=1
print("1 부터",num,"까지의 합:",result)
