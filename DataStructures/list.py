#LIST

'''
    It is a collection of data -[10,20,30]

        * mutable
        * ordered
        * changeable
        * allow duplicate values
        * allow different data types
        * indexed
'''
#-------------------------------------------------------------------------------------------
'''
a=[10,20,30,"Apple","Orange",10.5,10]
b=a[0],a[1]
c=a[3]
d=["Apple"]
for i in a:
    print(i)

print(type(b)) #tuple aah consider pannum

for i in c:
    print(i)

for i in d:
    print(i)
'''
#---------------------------------------------------------------------------------------------
'''
a=[10,20,30]
print(a[2::-1]) #len(a)-1

'''
#1. Append-------------------------------------------------------------------------------------------


'''
a=[10,20,30,"Apple","Orange",10.5,10]
a.append("Cherry")
print(a)
'''

'''
item=input("Enter an item/value: ")
a=[10,20,30,"Apple","Orange",10.5,10]
a.append(item)
print(a)
'''

'''
a=5
b=0
c=[]
for i in range(1,a+1):
    b+=i
    c.append(b)
print(c)
'''

'''
n=int(input("Enter Number: "))
fact=1
a=[]
for i in range(1,n+1):
    fact*=i
    a.append(fact)
print(a)
'''
#2.Extend-------------------------------------------------------------------------------------------
'''
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)

'''

#3.Clear 4.Copy-----------------------------------------------------------------------------
'''
a=10
b=a
print(id(a))
print(id(b))
'''
a=[1,2,3,4,5]
b=a.copy()
c=a
print(id(a))
print(id(b))
print(id(c))

#b.clear()
c.clear() # a also clear...same id value
print(a,c)
print(b)
print(a)

#Task-------------------------------------------------------------------------------------------

# oru list ulla int and str value mix aagi irukanum
# str oru list la add aaganum same for int(separate list)












