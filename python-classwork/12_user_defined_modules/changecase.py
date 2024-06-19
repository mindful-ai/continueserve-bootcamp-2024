s = input("Enter a string: ")
t = ""
for c in s:
    # if the char in upper case conv to lower
    if(c.isupper()):
        t += c.lower()
    # if in lower con to upper
    # store the string
    elif(c.islower()):
        t += c.upper()

# print the output
print(t)