#ITERATIVE STATEMENT

'''
1. For Loop

             used to over the sequence again and again unitl the condition gets true

        syntax:
                        for iterative in condition:
                            statement

-----------------------------------------------------------------------------------------'''
'''
for i in range(5):  #number- range
    print(i+1)

for i in "APPLE":
    print(i)
'''

#Task1----------------------------------------------------------------------------------
'''
num=int(input("Enter a Number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

'''
#----------------------------------------------------------------------------------------
'''
for i in range(5,0,-1):
    print(i)
'''
#--------------------------------------------------------------------------------------
'''
for i in range(1):
    print("UDHAYAA")
'''
#Task2-------------------------------------------------------------------------------------
'''
for i in range(10,0,-1):
    print(i,"x 2 =",i*2)
'''
#------------------------------------------------------------------------------------
'''
a=int(input("Enter a number: "))
for i in range(1,a+1):
    if i%2==0:
        print(i,"-Even")
    else:
        print(i,"-Odd")
'''
# -------------------------------------------------------------------------------------
'''
a=int(input("Enter a Value: "))
b=0
for i in range(a+1):
    b=b+i
print(b)
'''

#-------------------------------------------------------------------------------------
'''
a=10,25,3,99,7
b=0
for i in a:
    if i>b:
        b=i
print("Maximum Number is : ",b)

a=10,25,3,99,7
b=a[0]
for i in a:
    if i<b:
        b=i
print("Minimum Number is : ",b)

'''
#------------------------------------------------------------------------------------------
'''
for i in range(5):
    for j in range(i):
        print(j,end="")
    print()
'''

#Task3---------------------------------------------------------------------------------------
'''
name="UDHAYAA"
a=""
for i in name:
    a=i+a
print(a)

'''
#Task4-------------------------------------------------------------------------------------------
'''
a=input("Enter an Input: ").lower() 
vowels="aeiou"
b=[]
for i in a: 
    if i in vowels and i not in b:
        b.append(i)
print("No.of Vowels: ",len(b))

'''

#------------------------------------------------------------------------------------------
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''

#-----------------------------------------------------------------------------------------
'''
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
'''
#-----------------------------------------------------------------------------------------
'''
a="AKASH"
for i in range(len(a),0,-1):
    for j in range(i):
        print(a[j],end=" ")
    print()
'''
#------------------------------------------------------------------------------------------
'''
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

'''
#Task-------------------------------------------------------------------------------------------
'''
a=input("Enter your Name: ")

for i in range(len(a)):
    for j in range(i,len(a)):
        
        print(a[j],end=" ")
    print()
'''
    
#-------------------------------------------------------------------------------------------
'''
for row in range(1,4):
    print("Row-",row,end=": ")
    for seat in range(1,5):
        print("Seat",seat,end=" " )
    print()
'''

#-------------------------------------------------------------------------------------------
'''
a=int(input("Enter a Row Number: "))
b=int(input("Enter a Seat Number: "))

for row in range(1,4):  
    if a>3 or b>4:
        print("Please check that you've entered a valid row(1-3) and seat(1-4) number")
        break
    print("\nRow-",row,end=": \n")
    
    for seat in range(1,5):
            print("Seat",seat,end=" -  " )
            if row==a and seat==b:
                print(" Booked")
            else:
                print("Available")
'''
#-------------------------------------------------------------------------------------------
'''
c=[]
d=[]
for i in range(0,3):
    a=int(input("\nEnter a Row Number: "))
    b=int(input("Enter a Seat Number: "))


    if a in c and b in d:
        print("Already Booked")
    else:
        for row in range(1,4):  
            if a>3 or b>4:
                print("Please check that you entered a valid row(1-3) and seat(1-4) number")
                break 
            print("\nRow-",row,end=": \n")
    
            for seat in range(1,5):
                print("Seat",seat,end=" -  " )
                if row==a and seat==b:
                    print(" Booked")
                else:
                    print("Available")
    c.append(a)
    d.append(b)

'''            

                
#------------------------------------------------------------------------------------------
'''
for i in range(1,4):
    print("Customer: ",i)
    total=0
    item_count=int(input("Enter the no.of items: "))
    for j in range(1,item_count+1):
        price=int(input("Enter item price: "))
        total=total+price
    print("Total Bill: ",total)
    print("-------------------------------")
    
    
'''
#-------------------------------------------------------------------------------------------
'''
break-terminate the loop
continue-skip the loop
pass-acts as a placeholder

'''
'''
for i in range(61):
    if i%3==0 and i%5==0:
        continue
    print(i)
'''
#-------------------------------------------------------------------------------------------
'''
for i in range(10):
    if i==5:
        print(i)
        break
    else:
        print(i)
'''
#-------------------------------------------------------------------------------------------
'''
for i in range(10):
    pass
'''
#-------------------------------------------------------------------------------------------

a="udhaya@gmail.com","viswa@gmail.com","udhaya@proton.me","udhayaaa@gmail.in"
for i in a:
    if i.endswith(".com"):
        continue
    print(i)














