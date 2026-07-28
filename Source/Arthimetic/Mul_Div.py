def mul(a=10, b=20):
    return a * b

def div(a=100, b=20):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

