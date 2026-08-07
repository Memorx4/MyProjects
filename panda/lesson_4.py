import pandas as pd

df = pd.read_csv("data.csv")

print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

df["balance"] = df["balance"].fillna(df["balance"].median())
df["segment"] = df["segment"].fillna(df["segment"].mode()[0])


df["segment"] = df["segment"].str.lower().str.strip()

Q1 = df["balance"].quantile(0.25)
Q3 = df["balance"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["balance"] >= Q1 - 1.5 * IQR) & (df["balance"] <= Q3 + 1.5 * IQR)]
    

result = df.groupby("segment")["balance"].agg(["sum", "count", "mean"])
print(result)