def solution(n):
    string = str(n)
    num = 0
    sum = 0
    for i in string:
        i = string[num]
        sum += int(i)
        num += 1
    answer = sum
    return answer