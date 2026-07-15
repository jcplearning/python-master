import csv

with open('C:\\Jagan\\temp\\Product.csv','r') as csvfile:
    csvdata = csv.DictReader(csvfile,fieldnames=["product_id","product_name","concat","category_name","?column?","modify_date","class","resistant","isallergic","vitality_days"], delimiter=',')

    for data in csvdata:
        print(data)
