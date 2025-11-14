n = int(input("How many names? "))
for _ in range(n):
    name = input("Enter name: ")
    if len(name) > 5:
        print(name)
