n = int(input("Enter a number"))
cout =0
for i in range(1,n):
    if(n%i==0): 
        cout = cout+1
    else: 
        cout = 0

        if cout==0:
            print("N is a prime number")
        else :
            print("Not a prime number")