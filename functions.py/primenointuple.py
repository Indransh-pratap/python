def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

t = tuple(map(int, input("Enter numbers: ").split()))
count = sum(1 for x in t if is_prime(x))

print("Prime count =", count)
