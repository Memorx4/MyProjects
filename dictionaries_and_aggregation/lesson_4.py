import random
def anyls_transac(raw):
    data = {
        "MASS": 0,
        "MID": 0,
        "VIP": 0
    }
    new_list =[]
    for i in raw:
        if i > 0 and i <= 50000000:
            new_list.append(i)
    for i in new_list:
        if i < 7000000:
            data["MASS"] += i
        if 7000000 <= i < 25000000:
            data["MID"] += i
        if i >= 25000000:
            data["VIP"] += i
    return data

random_list = [random.randint(-5000000, 150000000) for i in range(100)]
print(random_list, sep=', ')
data = anyls_transac(random_list)
