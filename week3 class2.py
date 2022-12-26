class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self):
        super().__init__()#super is a keyword which helps us access the methods of the base class
        print("B init executed")
abc=B()

#Example
class SchoolMember:
    #Represents any school member
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        #Tell my details
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    #Represents a teacher
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
        print('Initialized Teacher:"{}"'.format(self.name))

    def tell(self):
        super().tell()
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    #represents a student
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        super().tell()
        print('Marks: "{:d}"'.format(self.marks))

t=Teacher("Mr. Ujjwal",40,30000)
s=Student("Nikhil",25,75)



#MRO(Method Resolution ORder)

class A:
    pass
class B(A):
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)
print(E.mro())

#DFS
#If there is a loop solve branches differently

#Iteration Protocol
#For any object to be an iterable,it should have 2 dunders
#__iter__
#__next__

#Protocol
#object's __iter__ method should return an iterator
#iterator's __next__ method should return the new value on every call
#if the iterator reaches the end,it should raise an StopIteration exception

a=range(5)
print(a)
it=a.__iter__()
print(it)
it.__next__()
print(next(it))

class myrange:
    def __init__(self,n):
        self.n
    def __iter__(self):
        pass
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret

for i in range(5):
    print(i)