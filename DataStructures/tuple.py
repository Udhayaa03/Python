#TUPLE

'''
    - Immutable
    - Unchangeable
    - Ordered
    - Indexed
    - Allow Duplicate Values
    - Allow different DataTypes
    - Much faster than list(less Memory)

    Example: (10,20,30,10)
'''
#-------------------------------------------------------------------------------------------
'''
a=(10,20,30,40,50,10,"python")
b=list(a) #To change convert to list --> change values 

b=a.count(10)
c=a.index(30)
print(b,c)


b.append(50)
print(b)
'''
a=(10,20,30,40,50,10,"python")
b=[]
for i in range(a[0]+1): 
    if i%2==0:
        b.append(i)
print(tuple(b))
