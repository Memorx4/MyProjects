import random 
random_list = [random.randint(10, 500) for i in range(12)]
max_val = random_list[0]
for i in random_list:
    if max_val < i:
        max_val = i
new_list =[]
for i in random_list:
    x = round(i / max_val, 2)  
    new_list.append(x)

print(new_list, sep=', ')
