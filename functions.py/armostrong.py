def is_armstrong(num):
    temp = num
    digits = len(str(num))
    sum_of_powers = 0
    while num > 0:
        rem = num % 10
        sum_of_powers += rem ** digits
        num //= 10
    return temp == sum_of_powers  