str = input("Enter string: ")


def double(str):
    for i in range(0, len(str)):
        print(str[i] + str[i], end='')


double(str)
