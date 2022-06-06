from audioop import reverse
from xml.dom.minidom import Element


n = int(input("Enter the number of elements in list: "))

print("Enter Elements:")

lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

srt = input("Enter the sorting order: ")


def sort(l, s):
    if s == 'asc':
        l.sort()
        print(l)
    elif s == 'desc':
        l.sort(reverse=True)
        print(l)
    elif s == 'none':
        print(l)


sort(lst, srt)
