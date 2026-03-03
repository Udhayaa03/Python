#DECORATORS:
'''
    Decorators are very powerful and useful tool in Python since
    it allows programs to modify the behaviour of a function or class
'''
#Example-------------------------------------------------------------------------------------------
'''
def Action(a):
    
    print("Thanks for Choosing")
    print("Welcome, Available cars are: ")
    b=["Benz","BMW","Kia","Toyoto"]
    for i in b:
        print(i)
    a()


@Action
def new():
    print("If you want something choose any one")

#Action(new)             #oru Function aah argument aah kodukurom

'''

#Logging Function Calls ------------------------------------------------------------------------------
'''
    Used in real projects to track which function runs.
'''

'''
def logger(fun):
    def wrapper():
        print("Function Started")
        fun()
        print("Function Ended")
    return wrapper

@logger
def work():
    print("Working")

work()
'''

#Login Authentication-------------------------------------------------------------------------------------------
'''
    Used in websites / apps to check user login before accessing page.
'''


def login_required(func):
    def wrapper():
        userLoggedIn=True

        if userLoggedIn:
            print("User Logged In")
            func()
        else:
            print("Please Login first")
            
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()

#Permission Check-------------------------------------------------------------------------------------------
'''
def AdminOnly(func):
    def wrapper():
        role=input("Enter Role: ")

        if role=="admin":
            print("Admin Logged In")
            func()
        else:
            print("Access Denied")
    return wrapper


users=["Udhayaa","Suresh","Babu"]

@AdminOnly
def CheckUser():
    a=input("Enter user to check: ")
    if a in users:
        print("User ",a," is Available")
    else:
        print("Unknown User")

CheckUser()
'''
#-------------------------------------------------------------------------------------------
















#GENERATOR-------------------------------------------------------------------------

'''
    Python generator is a way that specifies how to implement the iterators,
    It is a normal function expect that is ''yield" expression in the function
'''

#-------------------------------------------------------------------------------------------
'''
def fun():
    a=10
    b=20
    c=30
    yield a
    yield b
    yield c
var=fun()
print(next(var))
print(next(var))
print(next(var))
'''
#-------------------------------------------------------------------------------------------
'''
def fun():
    for i in range(10):
        yield i
        
b=fun()
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

'''


















