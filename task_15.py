sales = [
    {"product":"apple", "prise":3.00, "quantity":10},
    {"product":"bread", "prise":1.99, "quantity":20},
    {"product":"water", "prise":1.19, "quantity":15},
    {"product":"eggs", "prise":3.29, "quantity":20},
    {"product":"milk", "prise":1.59, "quantity":10}   
]

sum = 0
for x in sales:
    current_prise = x["prise"]
    current_q = x["quantity"]
    sum += current_prise*current_q

max_v = sales[0]["prise"]*sales[0]["quantity"]
product_maxv = sales[0]["product"]
for x in sales:
    current_v = x["prise"]*x["quantity"]
    if current_v>max_v:
        max_v = current_v
        product_maxv = x["product"]

unique_products = []

for x in sales:
    product_name = x["product"] 
    if product_name not in unique_products: 
        unique_products.append(product_name)

print("Общая сумма выручки:",sum)
print("Самый прибыльный продукт:",product_maxv,"Прибыль:",max_v)
print("Количество уникальных наименований:",len(unique_products))





