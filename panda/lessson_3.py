import pandas as pd

orders = [
    {"category": "Электроника", "price": 1000, "quantity": 2},
    {"category": "Аксессуары", "price": 50, "quantity": 5},
    {"category": "Электроника", "price": 150, "quantity": 3},
    {"category": "Одежда", "price": 500, "quantity": 1},
    {"category": "Аксессуары", "price": 100, "quantity": 4}
]
# 
df = pd.DataFrame(orders)

df["revenue"] = df["price"] * df["quantity"]

result = df.groupby("category")["revenue"].sum()

print(result)