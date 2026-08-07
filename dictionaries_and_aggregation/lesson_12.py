def category_sal(orders, category):
    sal = 0
    for i in orders:
        if i["category"] == category:
            sal = i["price"] * i["quantity"]
    return sal

orders = [
    {"item": "phone", "category": "electronics", "price": 5000, "quantity": 2},
    {"item": "book", "category": "others", "price": 500, "quantity": 5},
]
sal_elec = category_sal(orders, "electronics")
sal_othr = category_sal(orders, "others")
print(sal_elec, sal_othr)