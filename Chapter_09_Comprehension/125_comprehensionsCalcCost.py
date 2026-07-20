sales_data = [
    {"transaction_id": 1001, "date": "2026-01-01", "product": "Laptop", "quantity": 1, "unit_price": 1200.00, "region": "North"},
    {"transaction_id": 1002, "date": "2026-01-02", "product": "Mouse", "quantity": 2, "unit_price": 25.00, "region": "South"},
    {"transaction_id": 1003, "date": "2026-01-02", "product": "Monitor", "quantity": 1, "unit_price": 300.00, "region": "East"},
    {"transaction_id": 1004, "date": "2026-01-03", "product": "Keyboard", "quantity": 1, "unit_price": 75.00, "region": "West"},
    {"transaction_id": 1005, "date": "2026-01-04", "product": "Laptop", "quantity": 1, "unit_price": 1200.00, "region": "North"},
    {"transaction_id": 1006, "date": "2026-01-05", "product": "Mouse", "quantity": 5, "unit_price": 25.00, "region": "West"},
    {"transaction_id": 1007, "date": "2026-01-05", "product": "Monitor", "quantity": 2, "unit_price": 300.00, "region": "South"},
    {"transaction_id": 1008, "date": "2026-01-06", "product": "Laptop", "quantity": 1, "unit_price": 1200.00, "region": "East"},
    {"transaction_id": 1009, "date": "2026-01-07", "product": "Keyboard", "quantity": 3, "unit_price": 75.00, "region": "North"},
    {"transaction_id": 1010, "date": "2026-01-08", "product": "Mouse", "quantity": 1, "unit_price": 25.00, "region": "West"},
    {"transaction_id": 1011, "date": "2026-01-08", "product": "Monitor", "quantity": 1, "unit_price": 300.00, "region": "North"},
    {"transaction_id": 1012, "date": "2026-01-09", "product": "Laptop", "quantity": 2, "unit_price": 1200.00, "region": "South"},
    {"transaction_id": 1013, "date": "2026-01-10", "product": "Keyboard", "quantity": 1, "unit_price": 75.00, "region": "East"},
    {"transaction_id": 1014, "date": "2026-01-11", "product": "Mouse", "quantity": 2, "unit_price": 25.00, "region": "North"},
    {"transaction_id": 1015, "date": "2026-01-11", "product": "Monitor", "quantity": 1, "unit_price": 300.00, "region": "West"},
    {"transaction_id": 1016, "date": "2026-01-12", "product": "Laptop", "quantity": 1, "unit_price": 1200.00, "region": "South"},
    {"transaction_id": 1017, "date": "2026-01-13", "product": "Keyboard", "quantity": 4, "unit_price": 75.00, "region": "East"},
    {"transaction_id": 1018, "date": "2026-01-14", "product": "Mouse", "quantity": 3, "unit_price": 25.00, "region": "North"},
    {"transaction_id": 1019, "date": "2026-01-15", "product": "Monitor", "quantity": 2, "unit_price": 300.00, "region": "West"},
    {"transaction_id": 1020, "date": "2026-01-15", "product": "Laptop", "quantity": 1, "unit_price": 1200.00, "region": "South"},
    {"transaction_id": 1021, "date": "2026-01-16", "product": "Keyboard", "quantity": 1, "unit_price": 75.00, "region": "North"},
    {"transaction_id": 1022, "date": "2026-01-17", "product": "Mouse", "quantity": 1, "unit_price": 25.00, "region": "East"},
    {"transaction_id": 1023, "date": "2026-01-18", "product": "Monitor", "quantity": 1, "unit_price": 300.00, "region": "South"},
    {"transaction_id": 1024, "date": "2026-01-19", "product": "Laptop", "quantity": 2, "unit_price": 1200.00, "region": "West"},
    {"transaction_id": 1025, "date": "2026-01-20", "product": "Keyboard", "quantity": 2, "unit_price": 75.00, "region": "North"}
]

# Calculate the total sales for each transaction (quantity * unit_price) and store it in a new list using list comprehension

total_sales = [ sale.update({'cost': sale['quantity'] * sale['unit_price']}) or sale for sale in sales_data ]
print(f'The total sales for each transaction is {total_sales}')
