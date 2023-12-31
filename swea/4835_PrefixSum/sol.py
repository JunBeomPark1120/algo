import sys

sys.stdin = open('input.txt')

TC = int(input())

# 내 코드
# for tc in range(1, TC + 1):
#     N,M = map(int, input().split())
#     l = list(map(int, input().split()))
#     sum = []    # M개의 합을 저장할 수 있는 리스트 생성
#     result = 0
#     R_sum = 0   # 각 구간합 초기화
    
#     for i in range(N - M + 1) :
#         for j in range(M):
#             R_sum += l[j]
#         sum[i].append(R_sum)
#     sum.sort()
#     result = sum[0]
    
#     print(f'{tc} {result}')

for tc in range(1, TC + 1):
    N,M = map(int, input().split())
    
    numbers = list(map(int, input().split()))
    
    min_total = 1000000000
    max_total = 0
    # 구간합을 구하기 위한 i => 위의 n개의 데이터를 더하기 위한 시작점
    # index out of range : 에러를 발생시키지 않기 위해
    for i in range(N - M + 1) :
        
        total = 0
        # 시작점을 기준으로 오른쪽 M개를 구하기 위한 반복
        for j in range(M) :
            total = total + numbers[i + j]
        
        if total < min_total:
            min_total = total
            
        if total > max_total:
            max_total = total
            
    result = max_total - min_total

    print(f'#{tc} {result}')