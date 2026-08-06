def calculate_total_balance(clients_list, target_segment):
    total = 0
    for client in clients_list:
        if client["segment"] == target_segment:
            total += client["balance"] 
    return total

data = [
    {"name": "Alex", "segment": "vip", "balance": 20000000},
    {"name": "Charl", "segment": "mass", "balance": 2000000},
    {"name": "Mari", "segment": "mass", "balance": 4000000},
    {"name": "Kon", "segment": "mid", "balance": 9000000}
]

mass_total = calculate_total_balance(data, "mass")
mid_total = calculate_total_balance(data, "mid")
vip_total = calculate_total_balance(data, "vip")

print(f"Сумма по сегменту mass: {mass_total}")
print(f"Сумма по сегменту mid: {mid_total}")
print(f"Сумма по сегменту vip: {vip_total}")