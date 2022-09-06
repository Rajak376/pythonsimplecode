try:
    t = 5/0  
    print(t)
except ZeroDivisionError:
    print('exception is occurred')
    print("Can't divide by zero")
  
finally:
    print('This is always executed')

