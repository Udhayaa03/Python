a="I have an apple and apple colour is red"
print(a.replace("apple","orange",1))
#-------------------------------------------------------------------------------------

b=1234
b1=str(b)
print(type(b1))
print(b1[2],b1[1],b1[0],b1[3])
#-------------------------------------------------------------------------------------

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
#-------------------------------------------------------------------------------------

