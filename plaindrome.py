n = int(input("Enter a number: "))
original = n  
num = 0

while n > 0:
    rem = n % 10
    num = num * 10 + rem
    n = n // 10

if original == num:
    print("Palindrome")
else:
    print("Not a palindrome")
