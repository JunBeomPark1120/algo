def solution(n):
    answer = (n // 7) + 1
    if n % 7 == 0:  # 7명으로 나누어 떨어진 사람이 피자를 잡을 때
        answer = (n // 7)
    return answer

print(solution(7))
print(solution(1))
print(solution(15))