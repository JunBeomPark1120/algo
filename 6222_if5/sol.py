import sys
sys.stdin = open('input.txt')

char = input()

if char.isupper():
    # 대문자인 경우
    result = char.lower()
else:
    # 소문자인 경우
    result = char.upper()
    
print(char, result)
print(ord(char), ord(result))
print(f'{char}(ASCII)'ord(char), ord(result))