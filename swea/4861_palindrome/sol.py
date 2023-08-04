import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N : N * N 크기의 글자판 생성
    # M : 길이가 M인 회문 
    N,M = map(int, input().split())
    
    # 회문인 문장을 저장할 수 있는 문자열 생성
    p = ''
    
    for _ in range(N):
        # 입력받은 문자열을 담을 수 있는 문자열 초기화
        m = str(input())
        
        #입력받은 문자열의 끝 점 설정 및 시작 점 설정
        end = len(m)
        start = 0
        
        # 중간 지점 설정
        middle = (start + end) // 2
        
        # 체크
        ok = False
        
        # N의 크기와 M의 길이가 같다면?
        if N == M :
            for i in range(middle) :
                if m[end - i - 1] == m[start + i] :
                    ok = True
                else :
                    ok = False
            if ok == True:
                p = m
            else :
                continue 
                 
        # N과 M이 같지 않다면        
        else :
            #끝 점과 시작 점을 비교
            for i in range(middle):
                # 끝 점의 문자와 시작 점의 문자가 같지 않다면
                # 시작 점 오른쪽으로 위치시킴
                if start != end :
                    start = m[i]
                # 끝 점의 문자와 시작 점의 문자가 같다면
                # 회문 비교 시작
                # 끝 점의 인덱스 -1, 시작점의 인덱스 +1
                # middle만큼 반복하기 위해 middle값 초기화
                else :
                    middle = len(m) - m[i]
                    for j in range(middle // 2):
                        m[len(m) - 1 -j]
    print(f'#{tc} {p}')