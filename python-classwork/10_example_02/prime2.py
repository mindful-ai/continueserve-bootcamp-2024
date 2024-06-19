# Program to determine if a number is prime or not

n = int(input("Enter a number: "))


# --------------------------------- Start of task

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")
