
# Python program to demonstrate
# multilevel inheritance
 
# Base class
 
 
class stu:
 
    def __init__(self, name1):
        self.name1 = name1
 
# Intermediate class
 
 
class stu1(stu):
    def __init__(self, name1, name2):
        self.name2 = name2
 

        name1.__init__(self, name1)
 
# Derived class
 
 
class stu3(stu1):
    def __init__(self, name1, name2, name3):
        self.name3 = name3
 
        stu1.__init__(self, name2, name1)
 
    def print_name(self):
        print("name1 :", self.name1)
        print("name2 :", self.name2)
        print("name3 :", self.name3)
 
 
#  Driver code
s1 = stu3('Prince', 'Rampal', 'Lal mani')
print(s1.name3)
print(s1.name2)


