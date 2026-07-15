import json

with open('product.json','r') as f:
	productdata = json.load(f)
	print(type(productdata))

totalinventory = 0

for product in productdata:
    price = product['price']
    units = product['quantity']
    inventory = price * units
    totalinventory += inventory
print(f'Total inventory value: ${totalinventory:.2f}')

