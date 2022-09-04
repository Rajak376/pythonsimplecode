#reversing dictionary

d={'k1':1,'k2':2,'k3':3}
c={}
for i in reversed(d):
    c[i]=d[i]

print(c)
