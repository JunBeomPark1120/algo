import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def makeTree(n):
    global count
    # 배열이므로 배열 크기가 넘어가지 안도록 if설정
    if n <= N :
        # 왼쪽 노드는 현재 인덱스의 2배
        makeTree(n * 2)
        # 더 이상 못가면 값 넣기
        tree[n] = count
        # 값을 추가하면 1 증가
        count += 1
        # 우측 노드는 인덱스를 2 곱하고 1 더할 것
        makeTree(n * 2 + 1)
        
T = int(input())

for tc in range(1, T+1):
    # 테스트 케이스 별 N
    N = int(input())
    
    # 트리를 형성
    tree = [0] * (N + 1)
    
    count = 1
    
    makeTree(1)
    print(f"#{tc} {tree[1]} {tree[N // 2]}")
    
# 문제는 풀었지만 해당 문제는 중위순회방식으로 
# 푸는 것이 가장 좋다