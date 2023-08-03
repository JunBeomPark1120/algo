import sys

sys.stdin = open('input.txt')

TC = 10

for tc in range(1, TC + 1) :
    result = 0 # 세대수 초기화
    N = int(input())    # 건물의 개수
    S = list(map(int, input().split())) # 각 건물의 높이들
    for i in range(2, len(S) - 2):
        # 첫 번째 건물에서 부터 마지막 건물까지 비교하기
        
        # 선택된 건물 기준으로 왼,오 2칸의 건물이 낮은지 체크
        if ((S[i] > S[i - 1]) and (S[i] > S[i - 2])) and ((S[i] > S[i + 1]) and (S[i] > S[i + 2])):
            # 위의 조건이 만족되면 왼쪽 건물의 높이 비교
            max1 = 0 # 왼쪽 건물의 최대 높이
            max2 = 0 # 오른쪽 건물의 최대 높이
            max = 0 # 가장 높은 왼쪽 건물의 길이와 가장 높은 오른쪽 건물의 길이를 비교 후 제일 높은 건물로 초기화
            if S[i - 1] > S[i - 2]:
                max1 = S[i - 1]
            else :
                max1 = S[i - 2]
                
            # 위의 조건이 만족되면 마찬가지로 오른쪽 건물 높이 비교
            if S[i + 1] > S[i + 2]:
                max2 = S[i + 1]
            else :
                max2 = S[i + 2]
            
            # 가장 높은 왼쪽 건물과 가장 높은 오른쪽 건물 높이를 비교하기
            if max1 > max2:
                max = max1
            else :
                max = max2
                
            # 선택한 건물 기준으로 2번째로 높은 건물의 값 빼준 후 더하기
            result = result + S[i] - max
        else : # 그렇지 않으면 돌아가기
            continue
    print(f'#{tc} {result}')