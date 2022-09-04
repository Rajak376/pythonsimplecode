import csv

temp=['temp1','temp2','temp3']
colour=[['yellow','red','blue'],[1,2,3,4],[5,6,7,8,9],['t','y','u','o','p']]
n=[[],[],[],[],[]]
d={'k1':1,'k2':2,'k3':3}

with open('file1.txt','w') as file:

    writer=csv.writer(file)

    writer.writerow(temp)

    writer.writerow(colour)

    writer.writerow(n)

    writer.writerow(d)

