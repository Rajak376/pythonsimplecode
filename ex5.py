#bubble sort
a=[2,4,1,3,6,5,0,7,8,3,9,10]
for i in range (len(a)-1,0,-1):
    #print(i)
    for j in range(i):
        if a[j]>a[j+1]:
            temp=a[j]
            #print(temp)
            a[j]=a[j+1]
            a[j+1]=temp

print(a)
