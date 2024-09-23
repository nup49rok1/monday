# 17sortbubble.py
#https://passing-story.tistory.com/entry/Python-%EB%B2%84%EB%B8%94-%EC%A0%95%EB%A0%AC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B2%84%EB%B8%94-%EC%A0%95%EB%A0%AC
# 버블 정렬의 범용성을 높이기 위해 함수로 만듬
def bubbleSort(arr):
    n = len(arr) # 배열의 크기를 측정

    # 배열의 크기만큼 반복
    for i in range(n):
        
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):
            
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

# 예시 배열
arr = [64, 34, 25, 12, 57, 93, 1, 123]

bubbleSort(arr)

print("[Sorted array is]")
for i in range(len(arr)):
    print("%d " %arr[i], end = "")
    
'''
[Sorted array is]
1 12 25 34 57 64 93 123 
'''