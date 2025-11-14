n = int(input("Enter size: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

print("Reversed List:", lst[::-1])
