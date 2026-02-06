##a=20
##b=30
##a=b
##print(a+b)


##import keyword
##print(keyword.kwlist)


#a="10"
#b="10"
#print(a+b)

##a =10
##b="20"
##c=int(b)
##print(a+int(b))

##a=input("Enter your name :")
##age=int(input("Enter Your Age: "))
##print("Your name is",a,"and your age is",age)

name=input("Enter Name : ")
subject=int(input("Enter the no of subjects: "))
marks=[]
tot=0
for i in range(subject):
    mark=int(input(f"Enter mark{i+1} : "))
    marks.append(mark)
    tot+=mark
   # tot=tot+mark
    avg=tot/subject
print("\n\t\t\t STUDENT DETAILS")
print(f"Name : {name}\nMarks : {marks} ")
print(f"Total : {tot}")
print(f"Average : {avg}")


'''
mark1=int(input("Enter Mark1 : "))
mark2=int(input("Enter Mark2 : "))
mark3=int(input("Enter Mark3 : "))
mark4=int(input("Enter Mark4 : "))
mark5=int(input("Enter Mark5 : "))

total=mark1+mark2+mark3+mark4+mark5
average=total/5

print("\n\t\t\tStudent Details\n")
print(f"Name: {name}\nMark1:{mark1}\nMark2:{mark2}\nMark3:{mark3}\nMark4:{mark4}\nMark5:{mark5}")
print(f"\nTotal: {total}\nAverage: {average}")
'''

