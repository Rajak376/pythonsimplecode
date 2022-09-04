import csv

file=open('file.txt','w')

writer=csv.writer(file)

writer.writerow(['my name is razak shaik'])

file.close()
