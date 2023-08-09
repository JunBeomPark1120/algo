import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

 
tc = int(input())
 
for idx in range(1, tc+1):
    N = int(input())
 
    # 미로 받아오기 & 출발 지점 찾기
    maze = [list(map(int, input())) for _ in range(N)]
    
    # pprint(maze)
    # print()
    
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                maze[i][j] = -1
    # print(start)
    
    # dfs를 동작하기 위한 큐
    queue = []
    queue.append(start)
    # queue.append(start)
    
    #상하좌우 델타값
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    result = 0
    
    while len(queue):
        
        now = queue.pop(0)
        x, y = now[0], now[1]
        
        #  1  |  3  |  1  |  0  |  1
        #(0,0)|(0,1)|(0,2)|(0,3)|(0,4)
        #  1  |  0  |  1  |  0  |  1
        #(1,0)|(1,1)|(1,2)|(1,3)|(1,4)
        #  1  |  0  |  1  |  0  |  1
        #(2,0)|(2,1)|(2,2)|(2,3)|(2,4)
        #  1  |  0  |  1  |  0  |  1
        #(3,0)|(3,1)|(3,2)|(3,3)|(3,4)
        #  1  |  0  |  0  |  2  |  1
        #(4,0)|(4,1)|(4,2)|(4,3)|(4,4)
        
        # pprint(maze)
        # print()
        
        #상하좌우 방향을 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 안에 있다면 진행
            if 0 <= nx < N and 0 <= ny < N:
                # 길이라면?(길 == 0)
                if maze[nx][ny] == 0:
                    queue.append((nx,ny))
                    maze[nx][ny] = maze[x][y] - 1
                # 도착지점이라면?
                elif maze[nx][ny] == 3:
                    pass
                    result = abs(maze[x][y]) - 1
                    # 거리 계산 결과를 저장
        
    print(f'#{idx} {result}') 