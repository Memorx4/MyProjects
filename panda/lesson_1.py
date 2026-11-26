import pandas as pd

data = [
    {"name": "Alex", "segment": "vip", "balance": 20000000},
    {"name": "Charl", "segment": "mass", "balance": 2000000},
    {"name": "Mari", "segment": "mass", "balance": 4000000},
    {"name": "Kon", "segment": "mid", "balance": 9000000}
]

df = pd.DataFrame(data) 
print(df)

rich_clients = df[df["balance"] > 5000000]
print(rich_clients)