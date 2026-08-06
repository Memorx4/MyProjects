def calculate_category_revenue(list, target):
    total = 0
    for i in list:
        if i["category"] == target:
            total += i["price"]
    return total

orders =[
    {"item": "phone", "category": "electronics", "price": 5000},
    {"item": "laptop", "category": "electronics", "price": 10000},
    {"item": "book", "category": "others", "price": 500},
    {"item": "manga", "category": "others", "price": 200},
    {"item": "shower_gel", "category": "skincare", "price": 2000},
]
electro_total = calculate_category_revenue(orders, "electronics")
skincare_total = calculate_category_revenue(orders, "skincare")
others_total = calculate_category_revenue(orders, "others")
print(electro_total, skincare_total, others_total)
