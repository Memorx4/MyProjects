import random

random_list = [random.randint(1,100) for i in range(10)]
print(random_list)
for i in random_list:
    if i >= 60:
        print(i)