# Write a program to input a number and
# print the sum of individual digits

'''
Input -> 1234
Output -> 10
'''

# input
n = input("Enter a number: ")

# process

s = 0
if(n.isdigit()):
    for digit in n:
        s += int(digit)


# output
print("Sum of individual digits is ", s)