def sum_count(data, segment):
    new_data = {
        "balance": 0,
        "count": 0
    }
    for i in data:
        if i["segment"] == segment:
            new_data["count"] += 1 
            new_data["balance"] += i["balance"]
    return new_data

data = [
    {"name": "Alex", "segment": "vip", "balance": 20000000},
    {"name": "Charl", "segment": "mass", "balance": 2000000},
    {"name": "Mari", "segment": "mass", "balance": 4000000},
    {"name": "Kon", "segment": "mid", "balance": 9000000}
]
total_vip = sum_count(data, "vip")
total_mass = sum_count(data, "mass")
total_mid = sum_count(data, "mid")
print(total_mass, total_mid, total_vip)
