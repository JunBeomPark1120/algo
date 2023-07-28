def solution(n):
    answer = (n // 7) + 1
    if n % 7 == 0:
        answer = (n // 7)
    return answer

print(solution(7))
print(solution(1))
print(solution(15))