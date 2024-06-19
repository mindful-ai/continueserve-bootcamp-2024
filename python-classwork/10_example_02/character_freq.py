# Write a program to output the charater frequency of the input text

'''

Input <- apples
Output ->

a  ---> 1
p  ---> 2
l  ---> 1
e  ---> 1
s  ---> 1

'''


# input
text = input("Enter text: ")

# process

d = {}
for c in text:
    if(c in d.keys()):
        d[c] = d[c] + 1
    else:
        d[c] = 1

# output

for k, v in d.items():
    print(k , ' ---> ' , v)