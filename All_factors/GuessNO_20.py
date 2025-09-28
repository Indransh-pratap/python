import random
number1 = int(input("Enter the number: "))
number = random.randint(1,10)
if(number==number1):
    print("You guessed right ")
else:
    print("Please try again later")