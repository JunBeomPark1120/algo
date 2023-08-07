import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def paper_cut(n):
    # 1번 째 케이스
    if n == 1:
        return 1
    # 2번 째 케이스
    elif n == 2:
        return 3
    # n = 3, return 5
    # n = 4, return 11
    # n = 5, return 21
    # 3이상의 n은 n-1의 리턴값과 n-2의 리턴값에 2배를 더한 값으로
    # 점화식이 형성되었음.
    return paper_cut(n-1) + paper_cut(n-2) * 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = paper_cut(N//10)

    print("#{} {}".format(tc, ans))