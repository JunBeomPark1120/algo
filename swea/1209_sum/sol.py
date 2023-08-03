import sys

sys.stdin = open('input.txt')

TC = 10

for tc in range(1, TC + 1):
    tc = int(input())
    
    matrix = []

    #for문 중 _는 변수 활용을 하지 않을 예정이라 변수 이름을 비운다는 의미
    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    total = 0
    
    #가로줄 반복
    for row in range(len(matrix)):
        temp = 0
        for col in range(len(matrix[0])):
            temp += matrix[row][col]
        if total < temp:
            total = temp
            
    #세로줄 반복
    for col in range(100):
        temp = 0
        for row in range(100):
            temp += matrix[row][col]
            
        if total < temp:
            total = temp
            
    #최상단 => 우 하단 반복
    temp = 0
    for i in range(100):
        temp += matrix[i][i]
        
    if total < temp:
        total = temp
        
    #우상단 => 좌하단 반복
    temp = 0
    for i in range(100):
        temp += matrix[i][99-i]
        
    if total < temp:
        total = temp
        
    print(f'#{tc} {total}')