import sys

sys.stdin = open('input.txt')

TC = int(input())   # 테스트 케이스의 수

# 내 코드
# for tc in range(1, TC + 1):
#     l = [[]]  # 칠하고 싶은 영역 2차원 리스트로 선언
#     N = int(input())    #칠할 영역의 개수
#     for _ in range(N) :
#         area = list(map(int, input().split()))  #칠할 영역
        
#         r1 = l[0][0]    # 왼쪽 위 모서리 인덱스 시작점
#         c1 = l[0][1]    # 왼쪽 위 모서리 인덱스 끝점
        
#         r2 = l[0][2]    # 오른쪽 위 모서리 인덱스 시작점
#         c2 = l[0][3]    # 오른쪽 위 모서리 인덱스 끝점
        
#         # l(리스트)에 숫자를 대입하기
#         for i in range(r2 - r1):
#             for j in range(c2 - c1):
#                 if l[r1 + i][c1 + j] == 0:
#                     l[r1 + i][c1 + j] = l[0][4]
#                 else :
#                     continue
#     print(f'#{tc} {l}')

# 강사님 코드
for tc in range(1, TC + 1):
    N = int(input())
    board = [[0 for _ in range(10)] for _ in range(10)]

    # 이 코드와 동일
    # board = []
    # for _ in range(10):
    #     temp = []
    #     for _ in range(10):
    #         temp.append(0)
    #     board.append(temp)
    
    for i in range(N):
        # [2,2,4,4,1] => r1, c1, r2, c2, color
        color_data = list(map(int, input().split()))
        
        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]
        
        # 색칠시작
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color
                
    count = 0
    
    for x in range(board):
        for y in range(board[0]):
            if board[x][y] == 3:
                count += 1
    print(board)