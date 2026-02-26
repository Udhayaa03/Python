#Control Flow Statement
#Control flow is the order in which the program get execute

'''
1.Conditional Statement

    * if
    * if-else
    * if-elif-else
    * nested if

2.Iterative Statement

    * for
    * while

3.Transfer or Jump Statement -it alter the way a logic get executed

    * break
    * pass
    * continue
    
'''
#-----------------------------------------------------------------------------------------
'''
Mark=int(input("Enter your Mark: "))

if Mark<35:
    print ("Fail")
    
elif Mark>=35 and Mark<100:
    print("Pass")

else:
    print("Only Apsara user can score above 100...athukoda 5 than extra varum ")

'''
#------------------------------------------------------------------------------------------
'''
pin=1234
balance=10000
acc_no=4321

a=int(input("Enter your PIN: "))
b=int(input("Enter your Account Number: "))

if a==pin:
    print("\nYour PIN is Correct.")
    print("\n1.Balance Enquiry \n2.Deposit \n3.Withdraw")
    c=int(input("Enter an Option: "))
    
    if c==1:
        print(f"\nYour Balance is {balance}")
    elif c==2:
        amt=int(input("\nEnter an Amount to Deposit: "))
        total=balance+amt
        print(f"\nDeposited Amount: {amt} \nBalance: {total}")
    elif c==3:
         withdraw=int(input("Enter an amount to withdraw: "))
         
         if withdraw<=balance:
             amt=balance-withdraw
             print("\nCollect Your Payment.\nYour Balance amount is: ",amt)
         else:
            print("\nInsufficient Fund !..Your balance is: ",balance)
            
             
elif b==acc_no: 
    print("PIN is Incorrect but Account Number is Correct")
    print("\n1.Balance Enquiry \n2.Deposit")
    a=int(input("\nEnter an Option: "))
    if a==1:
        print("\n Your balance is ",balance)
    elif a==2:
        amt=int(input("\nEnter an Amount to Deposit: "))
        total=balance+amt
        print(f"\nDeposited Amount: {amt} \nBalance: {total}")
    else:
        print("Please enter a valid option")
        
    
else:
    print("Incorrect PIN")

'''



#Task 1-----------------------------------------------------------------------------------------
'''
age=int(input("Enter your Age: "))
salary=int(input("Enter your Salary: "))

if age >=25 and age<=35 and salary>35000:
    print("You're Eligible for PREMIUM CREDIT CARD")

elif age >=36 and age<=50 and salary>20000:
    print("You're Eligible for CREDIT CARD")

else:
    print("You're Not Eligible")
'''    
#Task 2--------------------------------------------------------------------------------------------

'''
password=input("Enter your Password: ")
if len(password)>=6:
     print("Password is 6 Characters long")
     if password[0].isupper():
         print("First Character is Caps")
         if password[-1]=="*":
             print("Last Character is *")
         else:
             print("Last Letter should be *")
         print("\nStrong Password")
     else:
         print("First Letter should be Caps")

else:
    print("\nsWeek Password")

'''

password=input("Enter your Password: ")
if len(password)>=6:
     if password[0].isupper() and  password[-1]=="*":
         print("Strong Password")
     else:
         print("Please enter a valid password with first Character Caps and Last character '*' ")

else:
    print("\nWeek Password")

#Task 3------------------------------------------------------------------------------------------

'''
a=input("Enter something: ")
b=str(a)
print("Reversed: ",b[-1::-1])

'''
#------------------------------------------------------------------------------------------
