import argparse

def calc_commission(salesamount:float, commissionpct:float):
    return (salesamount * commissionpct) /100

parser = argparse.ArgumentParser(description='Enter sales amount and commission percent')

parser.add_argument('--sales_amount', type=float, default=5000,help='Enter sales amount')
parser.add_argument('--commission_percent', type=float, default=10,help='Enter comission percent')

args = parser.parse_args()
print(args.sales_amount)
print(args.commission_percent)

# called from prompt
# 112_argumentparser.py --sales_amount=10000 --commission_percent=12.5
print(f'The commission amount is {calc_commission(args.sales_amount,args.commission_percent)}')