import random

random_list = [random.randint(50000, 20000000) for i in range(12)]
print(random_list, sep=', ')
mass = 0
mid = 0
vip = 0
for i in random_list:
    if i <3000000:
        mass += 1
    if 3000000 <= i < 10000000:
        mid += 1
    if i > 10000000:
        vip += 1
print(mass, mid, vip)