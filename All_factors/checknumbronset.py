s = set(map(int, input("Enter numbers: ").split()))
x = int(input("Enter number to search: "))

if x in s:
    print("Exists in set")
else:
    print("Does not exist")
