# removing special character in string
s="uday1234$&@$12310uday"
t=['@','$','&']
for i in t:
    s=s.replace(i,'')
print(s)
