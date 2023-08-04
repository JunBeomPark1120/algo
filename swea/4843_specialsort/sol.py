import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T + 1):
    # N : 정수의 개수
    N = int(input())
    
    # An : N개의 정수
    An = list(map(int, input().split()))
    
    # An 리스트를 sort하여 정렬
    An.sort()
    
    #정렬하고자 하는 리스트를 하나 생성
    l = []
        
    
    for i in range(len(An) // 2):
        # 최소값 초기화
        min = 10000
        # 최댓값 초기화
        max = 0
        # 리스트 내 최대값 찾은 후 max에 저장
        
        if max < An[len(An) - i - 1] :
            max = An[len(An) - i - 1]
            
            # l 리스트에 최대값 추가
            l.append(max)
        # 리스트 내 최소값 찾은 후 min에 저장
        if min > An[i]:
            min = An[i]
            
            # l 리스트에 최소값 추가
            l.append(min)

    b = list(map(str, l))
    a = ' '.join(b)
    print(f'#{tc} {a}')
