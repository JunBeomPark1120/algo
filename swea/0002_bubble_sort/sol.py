my_list = [1,6,2,3,8,7,0,9,5,4]

for i in range(len(my_list) - 1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]
        
        if left > right:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            
            # temp = my_list[j]
            # my_list[j] = my_list[j + 1]
            # my_list[j + 1] = temp
            
print(my_list)