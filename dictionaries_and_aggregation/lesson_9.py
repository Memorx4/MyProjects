import random

random_list = [random.randint(-5000, 5000) for i in range(10)]
print(random_list, sep=', ')
maxi = random_list[0]
mini = random_list[0]
for i in random_list:
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i

print(maxi, mini)