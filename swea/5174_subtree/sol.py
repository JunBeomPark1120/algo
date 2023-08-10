import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # 간선의 개수 E, 부모노드 N의 값
    E, N = list(map(int, input().split()))
    
    # 부모 자식 노드 번호의 쌍
    nodes = list(map(int, input().split()))
    
    left_node = [0] * (E + 2)
    right_node = [0] * (E + 2)
    
    for i in range(0, E * 2, 2):
        parent = nodes[i]
        child = nodes[i + 1]
        
        if left_node[parent] == 0:
            left_node[parent] = child
        else:
            right_node[parent] = child
            
    # print(left_node)
    # print(right_node)
    
    stack = [N]
    count = 0
    
    while stack :
        now = stack.pop()
        count += 1
        
        if left_node[now]:
            stack.append(left_node[now])
            
        if right_node[now]:
            stack.append(right_node[now])
            
    print(f'#{tc} {count}')