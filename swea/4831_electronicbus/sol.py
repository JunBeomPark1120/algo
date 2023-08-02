import sys

sys.stdin = open('input.txt')

TC = int(input())

# 내 코드
# for tc in range(1, TC + 1):
#     location = 0    # 현재 위치
#     count = 0  # 충전 횟수 초기화
#     K, N, M = map(int, input().split())    
#     # K : 한 번 충전으로 최대한 이동할 수 있는 정류장 수
#     # N : 0번에서 출발하여 도착하는 종점
#     # M : 충전기가 설치된 개수
#     l = list(map(int, input().split()))
#     # 충전기를 설치한 정류장의 번호를 리스트형태로 입력받기

#     # 최소 충전을 하려면 현재 위치에서 최대한 이동할 수 있는 방법이 효율적이라 판단
#     # 최대한(K만큼) 이동 후 이동 한 구간 내 충전기가 있는 정류소가 생기면
#     # 최대 이동한 거리와 충전소의 위치가 같으면 최대 이동한 거리에 위치
#     # 만약 지나쳤으면 최대 이동한 위치 기준으로 가까운 충전소에 위치
        
#     print(f'#{tc} {count}')

# 강사님 코드
for tc in range(1, TC + 1) :
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    
    bus_stop = list(map(int, input().split()))
    
    count = 0   #충전 횟수
    now = 0     #현재 위치
    
    # 충전할 필요가 없이 바로 도착하는 경우
    if K >= N :
        count = 0
    # 충전을 하면서 지나가야 할 때
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속해서 반복
        while now < N:
            # 현재 위치(now)에서 최대로 갈 수 있는 범위를 찾음.
            # 최대로 갈 수 있는 범위(now + k)부터 현재 위치까지 반복
            for i in range(now + K, now, -1):
                # 1. 최대 범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break
                
                # 2. 최대범위가 종점을 아직 넘지 않은경우
                if i in bus_stop:
                    # 가장 위에 있는 충전소로 이동
                    now = i
                    
                    # 충전을 하고 이동을 했으니 카운트 증가
                    count += 1
                    
                    # 마지막 충전소를 찾았으니 더 이상 후진할 필요 X
                    break
            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없다면? => 도착 불가능
            else:
                count = 0
                now = N
                
    print(f'#{tc} {count}')