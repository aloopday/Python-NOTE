def newFun():
    global x 
    x = "Welcome"
    print(x +" to hong kong ")
newFun()
print("Beijing is "+ x)

## use a global keyword if you want to change a global variable inside a 
# function.

a ="awesome"

def myfunc():
    global a
    a = "fantastic"
myfunc()
print("Python is " + a)

