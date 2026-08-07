def list_n(data):
    list_name = []
    for i in data:
        if i["balance"] >= 5000:
            list_name.append(i["Name"])
    return list_name

data = [
    {"Name": "Alex", "balance": 7500},
    {"Name": "Mari", "balance": 3000},
    {"Name": "Charl", "balance": 10000},
    {"Name": "Max", "balance":2500}
]
name_list = list_n(data)
print(name_list, sep=', ')