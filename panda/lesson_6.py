import pandas as pd
import numpy as np

raw_data = {
    'client_id': [201, 202, 203, 204, 202, 205, 206, 207, 208],
    'plan': [' Premium ', 'Basic', 'premium', 'STANDARD', 'Basic', 'Standard', None, 'basic', 'PREMIUM'],
    'tenure_months': [12, 3, None, 24, 3, 6, 1, 18, 36],
    'monthly_charges': [85.0, 25.0, 80.0, 50.0, 25.0, 45.0, 20.0, None, 99999.0]
}

df_telecom = pd.DataFrame(raw_data)

df_telecom = df_telecom.drop_duplicates()
df_telecom["plan"] = df_telecom['plan'].fillna(df_telecom["plan"].mode()[0])
df_telecom["plan"] = df_telecom["plan"].str.lower().str.strip()
df_telecom["monthly_charges"] = df_telecom['monthly_charges'].fillna(df_telecom["monthly_charges"].median())

Q1 = df_telecom["monthly_charges"].quantile(0.25)
Q3 = df_telecom["monthly_charges"]. quantile(0.75)
IQR = Q3 - Q1
df_telecom = df_telecom[(df_telecom['monthly_charges'] >= Q1 - 1.5 * IQR) & (df_telecom['monthly_charges'] <= Q3 + 1.5 * IQR)]

result = df_telecom.groupby("plan")["monthly_charges"].agg(["sum", "mean", "count"])
print(result)

