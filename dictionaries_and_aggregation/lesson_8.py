def average(list, departament):
    aver = 0
    sum = 0
    count = 0
    for i in list:
        if i["department"] == departament:
            count += 1
            sum += i["salary"]
    aver = sum / count
    return aver

employees = [
    {"name": "Ivan", "department": "IT", "salary": 8000000},
    {"name": "Olga", "department": "HR", "salary": 5000000},
    {"name": "Petr", "department": "IT", "salary": 9500000},
    {"name": "Anna", "department": "Sales", "salary": 6000000},
]
aver_IT = average(employees, "IT")
aver_HR = average(employees, "HR")
aver_Sales = average(employees, "Sales")
print(aver_HR, aver_IT, aver_Sales)