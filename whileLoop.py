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

PIN=1234
OTP=9876
total=10000

attempts=3
while attempts>=1:
    a=int(input("Enter PIN:"))
    if a==PIN:
        print("\nPIN is Correct")
        print("\n1.Balance Enquiry \n2.Deposit \n3.Withdraw")
        b=int(input("Enter an Option: "))

        if b==1:
            print("\t\t\t\t Balance Enquiry\n")
            c=int(input("Enter OTP: "))
            if c==OTP:
                print("OTP Verified")
                print(f"\nYour Balance is {total}")
            else:
                print("Wrong OTP")
                
        elif b==2:
            print("\t\t\t\t Deposit\n")
            c=int(input("Enter OTP: "))
            if c==OTP:
                print("OTP Verified")
                amt=int(input("\nEnter an Amount to Deposit: "))
                total=total+amt
                print(f"\nDeposited Amount: {amt} \nBalance: {total}")
            else:
                print("Wrong OTP")

        elif b==3:
            print("\t\t\t\t Withdraw\n")
            c=int(input("Enter OTP: "))
            if c==OTP:
                print("OTP Verified")
                withdraw=int(input("Enter an amount to withdraw: "))
                if withdraw<=total:
                    amt=total-withdraw
                    print("\nCollect Your Payment.\nYour Balance amount is: ",amt)
                else:
                    print("\nInsufficient Fund !..Your balance is: ",total)
            else:
                print("Wrong OTP")
                
##        if a==PIN and c==OTP and b==1 or b==2 or b==3:
##            break
      
    else:
        attempts-=1 
        print(f"Incorrect PIN...{attempts} times left")

    
else:
    print("Invalid Attempts .....Locked !")
    
        















