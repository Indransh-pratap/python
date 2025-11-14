n = int(input("How many key-value pairs? "))
d = {}

for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

key = input("Search key: ")

print(d.get(key, "Not Found"))
