#OPERATORS

'''
It Perform an operation on variables and values

Types of operators :

    1.Arithmetic operators 
    2.Assignment operator 
    3.Comparision operator
    4.Logical operators  
    5.Identity operators 
    6.Membership operator

-------------------------------------------------------------------------
1.Arithmetic operators---- it is the mathematical operation
    + add
    - sub
    * multiply
    / division
    % modulus
    ** Exponentiation
    // floordivision
'''

a=10
b=20
print(a+b) #Addition
print(a-b) #Subtraction

c=10
d=3
print(c*d) #Multiplication
print(c/d) #Division
print(c%d) #Modulus
print(c//d) #Floor Division
print(c**d) #Exponentiation


'''
-------------------------------------------------------------------------
2.Assignment Operator ----Assign a value to a Variable
'''
e=10
e+=20
print(x:=10) #Walrus Operator (x=10....print(x))

'''
------------------------------------------------------------------------
3.Comparison Operator----Comparing the two variables and values

    == equal to
    !=  not equal to
    >   greater than
    <   less than
    >= greater than or equal to
    <= less than or equal to

'''

f=10
g=20
h="20"
print(f==g)
print(f!=g)
print(f<g)
print(f>g)
print(f<=g)
print(f>=g)

print(id(f))
print(type(g))


'''
------------------------------------------------------------------------------------------
4.Logical Operators ---combine the conditions and given the result

        And                          Or                        NOT
    T   T    T             T    T    T                     T    F
    T   F     F             T   F     T                     F    T
    F   T     F             F   T     T
    F    F    F              F    F    F

'''

i=10
j=20
k="UDHAYAA"
l="AKASH"

print(i<=j and k!=l) # True if both are true
print(i<=j or k==l)  #True if anyone of them is true


##name=input("Enter Username: ")
##password=input("Enter Password: ")
##
##name1=input("Renter Username: ")
##password1=input("Renter Password: ")
##
##print(name==name1 and password==password1)

'''
----------------------------------------------------------------------------------------
5.Identity Operator ---comparing the object id of two variables

    * is
    * is not
'''

m=10
n=10

print(id(m))
print(id(n))

print(m is n)
print(m is not n)

'''
-------------------------------------------------------------------------------------------
6.Membership Operator ---used to check if the sequence presence in the object

    * in
    * not in
'''

o="This is the classroom"
print("T" in o) #if present true..Otherwise false
print("z" not in o) #if not present true

fruit="apple","orange","cherry"
print("a" in fruit)  #False 
print(fruit[-1::-1])


p=1234
print("3" in str(p))




