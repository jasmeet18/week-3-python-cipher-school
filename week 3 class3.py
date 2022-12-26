@@ -0,0 +1,67 @@
#Generators

a=[]
for i in range(1,100):
    a.append(i**2)
for x in a:
    print(x)

def generate_squares(n):
    a=[]
    for i in range(1,100):
        a.append(i**2)
    return a

#More readable function
#Eager loading-All the values we want to obtain are computed first and then return
#CPU intensive operation
def generate_squares(n):
    return[i**2 for i in range(1,n)]
for x in generate_squares(100):
    print(x)


#Lazy loading
#keyword:yield

def generate_squares(n):
    for i in range(1,n):
        yield i**2

for i in generate_squares(100):
    print(i)

it=iter(generate_squares(10))
print(it)

def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it=iter(func())
print(next(it))

from time import sleep
def func():
    print("started")
    yield
    sleep(5)
    print("ended")
print("hello")
it=iter(func())
next(it)
print("world")
next(it)

a=generate_squares(10)
print(type(a))

a=(i**2 for i in range(10))
for i in a:
    print(i)

print(iter(a))
print(next(a))
