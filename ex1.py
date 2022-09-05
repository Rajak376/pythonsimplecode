class stu():
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age

class stu1():
    def __init__(self,name2,age):
        self.name2=name2
        self.age=age

class stu2(stu,stu1):
    def __init__(self,name3,age,id1):
        self.name3=name3
        self.age=age
        self.id1=id1

p1=stu2('Razzak',25,1314)
print(p1.name3)
print(p1.age)
