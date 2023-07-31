def solution(num_list):
    answer = []
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1
    answer.append(even)
    answer.append(odd)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,5,7]))