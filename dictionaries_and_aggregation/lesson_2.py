import random

def clean_transact(raw):
    new_list = []
    for i in raw:
        if 0 < i < 10000000:
            new_list.append(i)
    return new_list

random_list = [random.randint(-10000000, 100000000) for i in range(15)]
print(random_list, sep=', ')
new_list = []
new_list = clean_transact(random_list)


