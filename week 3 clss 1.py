#Dunders(magic methods)(event methods)

a=5
print(isinstance(a,object))
print(isinstance(a,int))


def func():
    pass
print(type(func))


class A:
    name="samiksha"
    marks=30
print(type(A))
print(type(int))


class A:
    def __call__(self):
        print("You called me")
a=A()
print(type(a))
a()


def func():
    print("Hello")
func()
func.__call__()

for i in range(5):
    print(i)


a={"name":"Samiksha"}
a["name"]


class A:
    name="samiksha"
    def __init__(self,n):
        self.n=n


class Dog:
    kind="canine"
    def __init__(self, name):
        self.name=name
a=Dog("Maxx")
print(a.name)
print(a.kind)


class Dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_trick(self,trick):
        self.tricks.append(trick)
d1=Dog("Maxx")
d1.add_trick("fetch")
d1.add_trick("talk")
print(d1.tricks)
d2=Dog("Bella")
print(d2.tricks)