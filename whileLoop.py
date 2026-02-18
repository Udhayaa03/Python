#While Loop

'''
     it is a infinity loop .it is used to iterate again and again until
     the conditions get satisfied
'''
#------------------------------------------------------------------------------------------
'''
a=1
while a<=5:
    print(a)
    a+=1
print("Hello\n",a)
'''
#------------------------------------------------------------------------------------------
'''
a=5
while a>0:
    print(a)
    a-=1
'''
#--------------------------------------------------------------------------------------------
'''
a=100
while a>0:
    print(a)
    a-=20
'''
#-------------------------------------------------------------------------------------------
'''
a=1
while a<=10:
    if a==5:
        print("UDHAYAA")
    else:
        print(a)
    a=a+1
'''
#--------------------------------------------------------------------------------------------
'''
a=1
while a<=10:
    if a%2==0:
        print("Even")
    else:
        print("Odd")
    a=a+1
'''
#-------------------------------------------------------------------------------------------
'''
a=1
while a<=10:
    if a==5:
        for i in range(a):
            print(i)
    else:
        print(a)
    a=a+1
'''
#------------------------------------------------------------------------------------------
'''
otp=4567
a=1
#c=0
while a<=10 and not c:
    b=int(input("Enter OTP : "))
    if b==otp:
        print("Verified")
        #c=1
        #a+=10
        #a=10
    else:
        print("Incorrect")
    a=a+1
'''
#------------------------------------------------------------------------------------------
'''
a="aravindh","akash","balajii","dinesh"
b=0
while b<len(a):
    print(a[b])
    b=b+1
'''
#-------------------------------------------------------------------------------------------
'''
password="udhaya03"
attempts=1
while attempts<=3:
    a=input("Enter Password: ")
    if a==password:
        print("Password is correct.\nLogged In")
        break
    else:
        print("Your Password is Incorrect")
    attempts+=1

else:
    print("Locked")
'''
#Task1-------------------------------------------------------------------------------------------
'''
PIN=1234
OTP=9876
total=10000
check=4
attempts=3
while attempts>=1:
    a=int(input("\nEnter PIN:"))
    
    if a==PIN:
        print("\nPIN is Correct")
        
        while check>=1:
            print("\n1.Balance Enquiry \n2.Deposit \n3.Withdraw")
            b=int(input("Enter an Option: "))

            if b==1:
                print("\t\t\t Balance Enquiry\n")
                c=int(input("Enter OTP: "))
                if c==OTP:
                    print("OTP Verified")
                    print(f"\nYour Balance is {total}")
                else:
                    print("Wrong OTP")
                    break
                
            elif b==2:
                print("\t\t\t Deposit\n")
                c=int(input("Enter OTP: "))
                if c==OTP:
                    print("OTP Verified")
                    amt=int(input("\nEnter an Amount to Deposit: "))
                    total=total+amt
                    print(f"\nDeposited Amount: {amt} \nBalance: {total}")
                else:
                    print("Wrong OTP")
                    break

            elif b==3:
                print("\t\t\t Withdraw\n")
                c=int(input("Enter OTP: "))
                if c==OTP:
                    print("OTP Verified")
                    withdraw=int(input("Enter an amount to withdraw: "))
                    if withdraw<=total:
                        total=total-withdraw
                        print("\nCollect Your Payment.\nYour Balance amount is: ",total)
                    else:
                        print("\nInsufficient Fund !..Your balance is: ",total)
                        break
                else:
                    print("Wrong OTP")
                    break
            else:
                print("\nInvalid Option")
            check-=1
                
      
    else:  
        attempts-=1
        print(f"Incorrect PIN...{attempts} attempts left")

    
else:
    print("Invalid Attempts .....Locked !")
''' 
#-------------------------------------------------------------------------------------------

#factorial using for
n=int(input("Enter a Value: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"Factorial of {n} is {fact}")















