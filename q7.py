
n = int(input("Enter the number of elements in array: "))

print("Enter Elements:")
arr = []

for i in range(0, n):
    ele = int(input())
    arr.append(ele)


def frq(lis):
    lst = []
    for i in range(len(lis)):
        lst.append(lis.count(lis[i]))
    index = lst.index(max(lst))
    return lis[index]


print("Highest frequency element is: ")
print(frq(arr))
