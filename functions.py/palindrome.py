def is_palindrome(num):
    temp = num
    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num //= 10
    return temp == reverse