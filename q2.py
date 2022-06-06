num = input("Enter credit card number: ")


def ast(n):
    length = len(n)

    for i in range(0, length - 4):
        print("*", end='')

    for i in range(length - 4, length):
        print(n[i], end='')


ast(num)
