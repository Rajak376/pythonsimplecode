# sorting of list(normal sorting)
a=[2,4,3,5,1,6,9,7,8,10]
b=[]
while a:
    t=a[0]
    for i in a:
        if i<t:
            t=i
    b.append(t)
    a.remove(t)

print(b)
