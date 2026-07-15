# Given a list of (product, price, quantity) tuples, compute the total revenue.

product = [
    ("Laptop", 1000, 5),
    ("Smartphone", 500, 10),
    ("Headphones", 100, 20),
    ("Monitor", 300, 7)
]
total_revenue = 0
for item in product:
    price = item[1]
    quantity = item[2]
    total_revenue += price * quantity

print(f'Total revenue: ${total_revenue}') 

# Given a list of (name, score) tuples, return the name of the person with the highest score.

scores = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95)
]
highest_score = 0
top_scorer = ""
for name, score in scores:
    if score > highest_score:
        highest_score = score
        top_scorer = name

print(f'Top scorer: {top_scorer} with a score of {highest_score}')

#Remove duplicates from a tuple while preserving order.
mytuple = (1, 2, 3, 2, 4, 1, 5)
myset = set(mytuple)
print(tuple(myset)) 



