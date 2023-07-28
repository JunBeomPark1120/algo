def solution(angle):
    answer = 0
    if (angle > 0 and angle < 90):
        answer = 1
        return answer
    elif angle == 90:
        answer = 2
        return answer
    elif (angle > 90 and angle < 180):
        answer = 3
        return answer
    else:
        answer = 4
        return answer
    
print(solution(71))
print(solution(91))
print(solution(180))