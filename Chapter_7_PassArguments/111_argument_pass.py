import sys

# calculate sales commission amount by accepting sales amount & commission percent as arguments

print(sys.argv)
print(len(sys.argv))

# 111_argument_pass.py 10000 20 ( argument values)
print(f'commission is { (float(sys.argv[1]) * float(sys.argv[2]) )/100 }')