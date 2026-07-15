#Converty a list of tuples to a list of dictonaries 
sales = [('apple', 10), ('banana', 5), ('orange', 8), ('apple', 15), ('banana', 10)]
keys = ['product','quantity']

sales_dict = {}
sales_list = []
for sale in sales:
    sales_dict = dict(zip(keys, sale))
    sales_list.append(sales_dict) 
print(sales_list)

# Find the total quantity for each product (summarize the sale data)

total_sales = {}

for sale in sales_list:
    product = sale['product']
    quantity = sale['quantity']
    total_sales[product] = total_sales.get(product, 0) + quantity

print(total_sales)
