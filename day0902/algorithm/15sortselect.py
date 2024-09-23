# 15sortselect.py (선택정렬)

# 정렬할 배열
arr = [64, 25, 12, 22, 11]

# 배열의 길이만큼 반복문 실행
for i in range(len(arr)):

    # 가장 작은 값을 저장할 변수에 i를 초기화
    min_idx = i
    for j in range(i + 1, len(arr)):# range(1,5) i+1(두번째부터 불러오기위해)
        # 만약 가장 작은 값변수가 다음 인덱스의 값보다 클경우
        # 추가
        print('loop inner=>','i=>',i,'j=>',j)
        if arr[min_idx] > arr[j]:  # 0번째>1번째
            min_idx = j # 값을 변경
            #추가
            print('if문 내부 min_idx 출력=>',min_idx,'arr[min_idx]=>',arr[min_idx])

    # 값을 변경
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    #추가
    print('arr'+str([i])+'=>',str(arr[i]))
    print('arr['+str(min_idx)+']=>',arr[min_idx])
    

# 정렬한 배열을 출력
print("[Sorted array]")
for i in range(len(arr)):
    print("%d " %arr[i], end = "")
    
'''
loop inner=> i=> 0 j=> 1
if문 내부 min_idx 출력=> 1 arr[min_idx]=> 25
loop inner=> i=> 0 j=> 2
if문 내부 min_idx 출력=> 2 arr[min_idx]=> 12
loop inner=> i=> 0 j=> 3
loop inner=> i=> 0 j=> 4
if문 내부 min_idx 출력=> 4 arr[min_idx]=> 11
arr[0]=> 11
arr[4]=> 64
loop inner=> i=> 1 j=> 2
if문 내부 min_idx 출력=> 2 arr[min_idx]=> 12
loop inner=> i=> 1 j=> 3
loop inner=> i=> 1 j=> 4
arr[1]=> 12
arr[2]=> 25
loop inner=> i=> 2 j=> 3
if문 내부 min_idx 출력=> 3 arr[min_idx]=> 22
loop inner=> i=> 2 j=> 4
arr[2]=> 22
arr[3]=> 25
loop inner=> i=> 3 j=> 4
arr[3]=> 25
arr[3]=> 25
arr[4]=> 64
arr[4]=> 64
[Sorted array]
11 12 22 25 64
'''