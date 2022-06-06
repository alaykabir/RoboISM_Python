string = input("Enter the String: ")


def num(str):
    sum = 0
    for i in range(0, len(str)):
        if str[i].isnumeric() == True:
            sum = sum + int(str[i])

    print(sum)


num(string)
