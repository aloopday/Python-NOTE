x ="Awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# if you create global variable and local variable are same name 
# this variable will be local, and can only be used 
"""
    inside the funcition.
"""
 
a = "Hello"

def newFunc():
    a ="Hk"
    print("Welcome to " + a)
newFunc()
print("Python is " + a)
