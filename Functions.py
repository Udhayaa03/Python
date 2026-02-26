#FUNCTIONS
'''
    - Function is a block of code when it is called, it will be execute or run
    - Defined by "def" keyword
    - main purpose of function is Reusability of code

'''


#Defining a Function-------------------------------------------------------------------------
'''
def Fn_name():
    print(a)
    print("Hello")

def Fun():
    print("Good")

Fun()
Fun()
Fn_name()                #Calling (Using Function Name)

'''

#-------------------------------------------------------------------------------------------
'''
a=10                        #Global Variable
def Function():
    print(a)

    global b
    b=20                    #Local Variable
    print(b)

Function()                
print(a)            #Global variable enga venalum use pannalam
print(b)            #Local variable aa function ulla mattum tha use panna mudiyum
                       # outside la use pannanum na global keyword use pannanum
'''


#-------------------------------------------------------------------------------------------
'''
def fun():
    a=[10,20,30,"Python"]
    for i in range(a[0]):
        if i==5:
            print("Udhayaa")
            break
        else:
            print(i)
    b=1
    c=[]
    while b<a[0]:
        c.append(b)
        b=b+1
    print(c)
fun()
'''

#-------------------------------------------------------------------------------------------
'''
mark1=int(input("Enter Mark 1: "))
mark2=int(input("Enter Mark 2: "))
mark3=int(input("Enter Mark 3: "))

def Add():
   total= mark1+mark2+mark3
   print("\n\nTotal: ",total)
   match total:
       case 300:
           print("Good")
        break

Add()
'''

#Task---------------------------------------------------------------------------------------

a=int(input("Enter a Number: "))
b=0

def Sum():
    global b
    for i in range(1,a+1):
        b=b+i
    print(b)

Sum()

#--------------------------------------------------------------------------------------------
#lambda
#filter
#map
#reduce
#enumerate
#zip

#1.Positional Arguement------------------------------------------------------------------
'''
def fun(a,b,c):         #parameter
    print(a)
    print(b)
    print(c)

fun(10,20,30)
'''
               # --------------------------------------------------------------- #

'''
def var(a,b):
    print(a,b)
    
var(10,20)
'''
                # --------------------------------------------------------------- #
'''
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=int(input("Enter d: "))
def var(a,b):
    print("Value of a is: ",a,"\nValue of b is: ",b)
    
var(c,d)
var(a,b)
'''
                # --------------------------------------------------------------- #
'''                
def login(username,password):
    if username=="Admin" and password=="1234":
        print("\nLogin Successful")
    else:
        print("\nInvalid Credentials")

login(input("Enter username: "),input("Enter password: "))
'''
        
#2.Default Arguement------------------------------------------------------------------------
'''
def login(username="Admin",password="1234"): #default
    if username=="Admin" and password=="1234":
        print("\nLogin Successful")
    else:
        print("\nInvalid Credentials")

login()
#login("admin","1234")                  #ipdi kodutha intha value thaan edukum
'''

#3.Non-keyword Arguement------------------------------------------------------------------
'''
def fun(*a):
    print(type(a))
    for i in list(a):
        print(i)

fun(5,6,7,8,9,10)
'''





