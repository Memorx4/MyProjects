import random

random_list = [random.randint(1, 1000) for i in range(10)]
print(random_list, sep=", ")
print(len(random_list))
sum = 0
for i in random_list:
    sum += i
print(sum)