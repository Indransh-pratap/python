n = int(input("How many strings? "))
t = tuple(input("Enter string: ") for _ in range(n))
print("Smallest (Dictionary Order):", min(t))
