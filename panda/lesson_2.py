import pandas as pd
import numpy as np

data = {
    'Имя': ['Анна', 'Иван', 'Ольга', 'Иван', 'Петр', 'Анна', 'Сергей', 'Мария', 'Иван'],
    'Возраст': [25, 30, 22, 30, 35, 25, 40, None, 30],
    'Зарплата': [1200, 1500, 1100, 1500, 1800, 1200, 2000, 1300, 50000] 
}

df = pd.DataFrame(data)

print("--- ИСХОДНЫЙ 'ГРЯЗНЫЙ' DATAFRAME ---")
print(df)

df = df.drop_duplicates()

print("--- ПОСЛЕ УДАЛЕНИЯ ДУБЛИКАТОВ ---")
print(df)

median_age = df['Возраст'].median()
df['Возраст'] = df['Возраст'].fillna(median_age)

Q1 = df['Зарплата'].quantile(0.25)
Q3 = df['Зарплата'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Зарплата'] >= lower_bound) & (df['Зарплата'] <= upper_bound)]

print("--- ФИНАЛЬНЫЙ ОЧИЩЕННЫЙ DATAFRAME ---")
print(df)