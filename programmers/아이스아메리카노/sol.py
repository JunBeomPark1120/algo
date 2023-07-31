def solution(money):
    answer = []
    coffee = money // 5500
    seed = money - (coffee * 5500)
    answer.append(coffee)
    answer.append(seed)
    return answer

print(solution(5500))
print(solution(15000))