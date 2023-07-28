import sys
sys.stdin = open('input.txt')

# 내 코드
# blood_type = ['A','A','A','O','B','B','O','AB','AB','O']

# dict = {'A':0,'B':0,'O':0,'AB':0}
# num = 0
# for i in blood_type:
#     if blood_type[num] == 'A' :
#         dict[0].values += 1
#         num += 1
#     if blood_type[num] == 'B' :
#         dict[1].values += 1
#         num += 1
#     if blood_type[num] == 'O' :
#         dict[2].values += 1
#         num += 1
#     if blood_type[num] == 'AB' :
#         dict[3].values += 1
#         num += 1
        
# print(dict)

# 강사님 코드
blood_type = ['A','A','A','O','B','B','O','AB','AB','O']

blood_dict = {
    'A' : 0,
    'B' : 0,
    'AB' : 0,
    'O' : 0
}

for blood in blood_type:
    blood_dict[blood] += 1
    
print(blood_dict)

# location_list = ['서울','부산','서울','서울','대전','제주','광주','부산']

# location_dict = {}

# for location in location_list:
#     #이미 기록을 한 경우
#     if location in location_dict.keys():
#         location_dict[location] += 1
#     # 처음 등장한 경우
#     else:
#         location_dict[location] = 1
        
# print(location_dict)