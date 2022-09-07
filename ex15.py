#  sapareting characters numbers and special symblos in given string by using string inbulid functions

a="uday1234$&@$123uday"
b=''
c=''
d=''

for i in a:
    if i.isnumeric():
        b=b+i

    elif i.isalpha():
        c=c+i
    else:
        d=d+i
print(b)
print(c)
print(d)



    
