# sapareting characters numbers and special symblos in given string by using conditions
s="uday1234$&@$123uday"
b=''
c=''
d=''
for i in range(len(s)):
    if (s[i].isdigit()):
        b=b+s[i]
        #print(b)
    elif ((s[i] >= 'A' and s[i]<= 'Z') or (s[i] >= 'a' and s[i]<= 'z')):
        c=c+s[i]
    else:
        d=d+s[i]

print('numbers',b)
print('characers',c)
print('special symbols',d)
        
        
