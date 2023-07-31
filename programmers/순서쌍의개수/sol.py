def solution(n):
    answer = 0
    # 약수의 개수를 구하면 끝나는 문제
    for i in range(1,n + 1):
        if n % i == 0:
            answer += 1
    return answer

print(solution(20))
print(solution(100))