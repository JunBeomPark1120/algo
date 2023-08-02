my_list = [1,2,3,3,5,6,8,4,3,5]

counter = [0 for i in range(10)]
for i in my_list:
    counter[i] += 1
    
result = []

for value, count in enumerate(counter) :
    for i in range(count):
        result.append(value)
        
print(result)