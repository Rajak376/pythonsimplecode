# palandrom of number

number=input(("Enter a number:"))
if(number==number[::-1]):
      print("The number is a palindrome")
else:
      print("Not a palindrome")
# onther methode

a=101
res=0
t=a
while t!=0:
      rem=t%10
      res=res*10+rem
      t=t//10
      
if res==a:
      print('palandrom')
else:
      print('not palandrom')
