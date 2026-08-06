random_list = [3, 2, 3, 5, 4, 2, 3, 7, 7, 8]
new_lest = []
for i in random_list:
    if i not in new_lest:
        new_lest.append(i)
new_lest.sort()
print(new_lest, sep=', ')