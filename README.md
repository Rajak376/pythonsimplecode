# pythonsimplecode
# sorting of list
a=[3,2,5,6,9,10]
print(sorted(a))

#list reverse

a=[1,3,2,4]
print(a[::-1])

#searching error in file

with open('file.txt') as f:
    if 'error' in f.read():
        print('error found')

# palandrom of number

number=input(("Enter a number:"))
if(number==number[::-1]):
      print("The number is a palindrome")
else:
      print("Not a palindrome")

#factorial number using recursion

def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
n=5
print(fact(n))

#reversing dictionary

d={'k1':1,'k2':2,'k3':3}
c={}
for i in reversed(d):
    c[i]=d[i]

print(c)

# spliting string at any one character

import re

txt = "The rain in Spain"
x = re.split("a", txt)
print(x)



