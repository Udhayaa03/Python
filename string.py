##'''
####a=20
####b=30
####a=b
####print(a+b)
##
##
####import keyword
####print(keyword.kwlist)
##
##
###a="10"
###b="10"
###print(a+b)
##
####a =10
####b="20"
####c=int(b)
####print(a+int(b))
##
####a=input("Enter your name :")
####age=int(input("Enter Your Age: "))
####print("Your name is",a,"and your age is",age)
##
##name=input("Enter Name : ")
##subject=int(input("Enter the no of subjects: "))
##marks=[]
##tot=0
##for i in range(subject):
##    mark=int(input(f"Enter mark{i+1} : "))
##    marks.append(mark)
##    tot+=mark
##   # tot=tot+mark
##    avg=tot/subject
##print("\n\t\t\t STUDENT DETAILS")
##print(f"Name : {name}\nMarks : {marks} ")
##print(f"Total : {tot}")
##print(f"Average : {avg}")
##
##
##'''
##mark1=int(input("Enter Mark1 : "))
##mark2=int(input("Enter Mark2 : "))
##mark3=int(input("Enter Mark3 : "))
##mark4=int(input("Enter Mark4 : "))
##mark5=int(input("Enter Mark5 : "))
##
##total=mark1+mark2+mark3+mark4+mark5
##average=total/5
##
##print("\n\t\t\tStudent Details\n")
##print(f"Name: {name}\nMark1:{mark1}\nMark2:{mark2}\nMark3:{mark3}\nMark4:{mark4}\nMark5:{mark5}")
##print(f"\nTotal: {total}\nAverage: {average}")
##'''
##
##
##'''






##String- it is the sequence of characters and it is enclosed with single and double quotes . it is immutable because it is unchangeable.

##1.Capitalize

a="Hello PYthoN"
print(a.capitalize())
print(a.title())

b="Hello pyThoN GoOD MoRNiNg"
print(b.lower())
print(b.upper())
print(b.swapcase())



##indexing is the process of accessing a specific element in a sequence....negative indexing starts with -1 and positive indexing starts with 0

c="PYTHON"
print(c[1]) #Positive indexing
print(c[-4]) #Negative Indexing

d="Apple","Orange","Cherry"
print(d[0][3])


##Length

e="Hello World"
print(len(e))

print(a.casefold())## works same as lower
print(a.center(20))
print(a.index("o")) #displays the index value of the z
print(a.rindex("o")) # checks for "o" from right and return the index value from left
print(a.find("z")) # same as index however if an unknown value is provided,  then shows -1


f="Apple","Banana","Cherry"
print(" ,".join(f))#Join using ','

g="UDHAYAA"
print(g.isupper())
print(g.islower())

##h=input("Enter name:")
##print(h[0].isupper())


#format() method is used to insert values into a string using {} placeholders
'''
name=input("Enter Name: ")
age=int(input("Enter Age :"))
print("Your Name is {1} and your age is {0}".format(name,age)) # if the index  is changed ..the values also changes based on the index
'''

i="NAME"
j="1234"
k="Name123"
print(i.isalpha())
print(j.isnumeric())
print(k.isalnum())

l="This is my Laptop"
print(l.replace("Laptop","Mobile"))

##length and count starts with 1







