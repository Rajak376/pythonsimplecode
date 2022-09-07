# removing character in string
s="uday1234$&@$12310uday"
x=''
y=''
z=''
for i in s:
    if not i.isalpha():
        x=x+i
print(x)
