n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

n1 = n1 ^ n2
n2 = n1 ^ n2
n1 = n1 ^ n2

print("After Swap")
print("first number: ", n1, " and second number: ", n2)
