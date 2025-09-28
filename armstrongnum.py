n = int(input("Enter a number: "))
original = n
sum = 0
num_len = len(str(n))

while n > 0:
    rem = n % 10
    sum += rem ** num_len
    n = n // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
