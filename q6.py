
low = int(input("Enter lower bound of the interval: "))
upp = int(input("Enter upper bound of the interval: "))


def prime(num):
    if(num == 2):
        return True
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


for i in range(low, upp + 1):
    if(prime(i)):
        print(i)
