# sum of sales 
def sum_sales(*sales):
    sales_amt = 0 
    if len(sales) == 0:
        return 0
    
    for sale in sales:
        if sale is not None:
            sales_amt += sale

    return sales_amt

print(f'The sum of the sales is {sum_sales(*(100.45, 200.30, 150.25))}')

list1 = []
print(f'The sum of the sales is {sum_sales(*list1)}')

list2 = [ 100.45, 200.30, None, 150.25 ]
print(f'The sum of the sales is {sum_sales(*list2)}')




