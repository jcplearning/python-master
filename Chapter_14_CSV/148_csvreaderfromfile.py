import csv

with open('C:\\Jagan\\temp\\Product.csv',mode='r') as csvfile:
    csvdata = csv.reader(csvfile,delimiter=',',quotechar='"',lineterminator='\n')
    print(type(csvdata))
    for data in csvdata:
        print(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])

print(f'The total no. of lines read from the source file is {csvdata.line_num}')
