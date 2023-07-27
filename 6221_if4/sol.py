# 내 코드
# import sys
# sys.stdin = open('input.txt')

# Man1 = input()
# Man2 = input()

# if (Man1 == '바위') & (Man2 == '바위'):
#     print('Result : Draw')
# elif (Man1 == '바위') & (Man2 == '가위'):
#     print('Result : Man1 Win!')
# elif (Man1 == '바위') & (Man2 == '보'):
#     print('Result : Man2 Win!')
# elif (Man1 == '가위') & (Man2 == '바위'):
#     print('Result : Man2 Win!')
# elif (Man1 == '가위') & (Man2 == '가위'):
#     print('Result : Draw')
# elif (Man1 == '가위') & (Man2 == '보'):
#     print('Result : Man1 Win!')
# elif (Man1 == '보') & (Man2 == '바위'):
#     print('Result : Man1 Win!')
# elif (Man1 == '보') & (Man2 == '가위'):
#     print('Result : Man2 Win!')
# elif (Man1 == '보') & (Man2 == '보'):
#     print('Result : Draw')

# 강사님 코드
# import sys
# sys.stdin = open('input.txt', encoding='utf-8')

# Man1 = input() # 가위
# Man2 = input() # 바위

# rcp = ['가위','바위','보']

# man1_idx = rcp.index(Man1)
# man2_idx = rcp.index(Man2)

# print(man1_idx,man2_idx)

# result = man1_idx - man2_idx

# if result == 0:
#     print('Result : Draw')
# elif result > 0:
#     print(f'Result : Man{result} Win!')
# else:
#     if result == -1:
#         print('Result : Man2 Win!')
#     else:
#         print('Result : Man1 Win!')
# # 가위, 바위, 보
# #  0     1    2

# # 보, (가위)    win2    2
# # (바위), 가위  win1    1
# # (보), 바위    win1    1
# # 가위, (바위)  win2    -1
# # 바위, (보)    win2    -1
# # (가위), 보    win1    -2