import pandas as pd
import numpy as np

raw_data = {
    'order_id': [101, 102, 103, 104, 102, 105, 106, 107, 108],
    'category': [' Electronics ', 'Clothing', 'Electronics', 'Home', 'Clothing', None, ' home', 'Clothing', 'Electronics'],
    'amount': [150.0, 45.0, 120.0, 80.0, 45.0, 200.0, None, 50.0, 1000000.0]
}

df_orders = pd.DataFrame(raw_data)

df_orders = df_orders.drop_duplicates()
df_orders["amount"] = df_orders["amount"].fillna(df_orders["amount"].median())
df_orders["category"] = df_orders["category"].fillna(df_orders["category"].mode()[0])
df_orders["category"] = df_orders["category"].str.lower().str.strip()

Q1 = df_orders["amount"].quantile(0.25)
Q3 = df_orders["amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_orders = df_orders[(df_orders["amount"] >= lower_bound) & (df_orders["amount"] <= upper_bound)]
result = df_orders.groupby("category")["amount"].agg(["sum", "count", "mean"])
print(result)