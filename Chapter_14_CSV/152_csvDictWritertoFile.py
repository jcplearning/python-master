import csv

mylist = [
{'product_id': '1', 'product_name': 'Flour - Whole Wheat', 'concat': 'Category 3', 'category_name': 'Cereals', '?column?': 'All Product', 'modify_date': '2018-02-16 08:21:49.19', 'class': 'Medium', 'resistant': 'Durable', 'isallergic': 'Unknown', 'vitality_days': '0.00'},
{'product_id': '2', 'product_name': 'Cookie Chocolate Chip With', 'concat': 'Category 3', 'category_name': 'Cereals', '?column?': 'All Product', 'modify_date': '2017-02-12 11:39:10.97', 'class': 'Medium', 'resistant': 'Unknown', 'isallergic': 'Unknown', 'vitality_days': '0.00'},
{'product_id': '3', 'product_name': 'Onions - Cippolini', 'concat': 'Category 9', 'category_name': 'Poultry', '?column?': 'All Product', 'modify_date': '2018-03-15 08:11:51.56', 'class': 'Medium', 'resistant': 'Weak', 'isallergic': 'False', 'vitality_days': '111.00'},
{'product_id': '4', 'product_name': 'Sauce - Gravy, Au Jus, Mix', 'concat': 'Category 9', 'category_name': 'Poultry', '?column?': 'All Product', 'modify_date': '2017-07-16 00:46:28.88', 'class': 'Medium', 'resistant': 'Durable', 'isallergic': 'Unknown', 'vitality_days': '0.00'},
{'product_id': '5', 'product_name': 'Artichokes - Jerusalem', 'concat': 'Category 2', 'category_name': 'Shell fish', '?column?': 'All Product', 'modify_date': '2017-08-16 14:13:35.43', 'class': 'Low', 'resistant': 'Durable', 'isallergic': 'True', 'vitality_days': '27.00'}
]

with open('C:\\Jagan\\temp\\Product_dictcopy.csv','w') as csvfile:
    csvdata = csv.DictWriter(csvfile,fieldnames=["product_id","product_name","concat","category_name","?column?","modify_date","class","resistant","isallergic","vitality_days"], delimiter='|',quotechar='"', quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
    csvdata.writeheader()
    for data in mylist:
        csvdata.writerow(data)
