import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

#강사님 코드
T = int(input())

memo = [0 , 1 , 3]

for tc in range(1, T + 1):
    N = int(input()) // 10
    
    #memo배열에 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-2 배열에 가로로 작은 사각형 두 개를 쌓거나 큰 사각형을 쌓는 방법(x2)
        # n-1 배열에 세로로 작은 사각형을 쌓는 방법 하나
        temp = 2 * memo[len(memo) - 2] + memo[len(memo) - 1]
        memo.append(temp)
        
    print(f'#{tc} {memo[N]}')