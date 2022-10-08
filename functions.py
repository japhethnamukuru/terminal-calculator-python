def convert(num):
    try:
        num = int(num)
    except ValueError:
        try:
            num = float(num)
        except ValueError:
            return None
        else:
            return num
    else:
        return num
        

operators = ['+', '-', '*', '/', '**']

def getOperation(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    elif op == '**':
        return a ** b
    else:
        return None
