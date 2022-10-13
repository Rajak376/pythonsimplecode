def myFunction(g=0,h=9,*args,u=0,y=90, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    myFunction("hello","ksdjk","jkjdksa", a = 24, b = 67, c = 3, d = 46)
    sum=myFunction(l=0,m=9)
    
