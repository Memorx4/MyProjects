import random
def segment_clien(sum_list):
    data = {"MASS": 0, "MID": 0, "VIP": 0}
    
    for i in sum_list:
        if i < 3000000:
            data["MASS"] += 1
        elif 3000000 <= i <= 10000000:
            data["MID"] += 1
        else:
            data["VIP"] += 1
            
    return data

random_list = [random.randint(0, 30000000) for i in range(7)]
print(random_list, sep=', ')
for i in random_list:
    if i >= 20000000:
        random_list.remove(i)
data = segment_clien(random_list) 
print(data)