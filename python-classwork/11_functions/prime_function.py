# Write a function checkprime which returns True if the number is prime and False otherwise

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# Function to find the smallest and largest
# prime numbers in a given range

def getPrimes(start, end):
    pass

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if(checkprime(n)):
        print("The number is prime")
    else:
        print("The number is  not prime")