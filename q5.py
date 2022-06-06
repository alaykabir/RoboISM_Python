lst = []

print("Enter Array elements: ")
for i in range(0, 100):
    ele = int(input())
    lst.append(ele)


def duplicate(lst):
    for i in range(0, 100):
        for j in range(0, 100):
            if lst[i] == lst[j]:
                print(lst[i])
