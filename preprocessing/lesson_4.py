import random

random_list = [random.randint(1, 1000) for i in range(10)]
print(random_list, sep=", ")
max_val = random_list[0]
min_val = random_list[0]
for i in random_list:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
    
print(f"максимум {max_val}", sep='\n')
print(f"минимум {min_val}")