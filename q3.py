n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("Enter operation: ")


def operation(x, oper, y):
    if oper == '+':
        print(x + y)
    elif oper == '-':
        print(x - y)
    elif oper == '.':
        print(x * y)
    elif oper == '/':
        print(x / y)


operation(n1, op, n2)
