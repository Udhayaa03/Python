'''
a="I have an apple and apple colour is red"
print(a.replace("apple","orange",1))
'''
#-------------------------------------------------------------------------------------
'''
b=1234
b1=str(b)
print(type(b1))
print(b1[2],b1[1],b1[0],b1[3])
'''
#-------------------------------------------------------------------------------------
'''
mark=int(input("Enter your Marks : "))
if mark<35:
    print("Fail")
elif mark>=35 and mark<50:
    print("Grade 'C'")
elif mark>=50 and mark<70:
    print("Grade 'B'")
elif mark>=70 and mark<90:
    print("Grade 'A'")
elif mark>=90 and mark<=100:
    print("Grade 'O'")
else:
    print("Undefined Mark. Please enter a a valid one")

'''
#-------------------------------------------------------------------------------------


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
    
        

