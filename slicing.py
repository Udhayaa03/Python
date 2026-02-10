##SLICING
'''
It is used to slice a sequence you can specify where to start the slicing and where to end

[start:]
[:end]
[start:end]
[start:end:step]

'''
##-------------------------------------------------------------------------------------------

a="APPLE IS MY FAV FRUIT"
print(a[16:]) #start 
print(a[:16]) #end (kodukum pothu oru value add panni kodukanum so that n-1 nu edukum)
print(a[12:15])
print(a[-9:-6])

b="This is an Apple"
print(b[11::2]) #start:end:step
print(b[-1:-6:-1]) #reverse la print aaganum na step value  -1 la irunthu kodukanum so that  ellam print aagum otherwise blank -aah thaan irukkum

fruits="Apple","Orange","Banana","Cherry","Mango","Grapes"
print(fruits[1][-1:-5:-1])

c="Apple","Orange","Banana","Che11rry","Mango","Grapes"
d=int(c[3][3:5])+10
print(d)

e="Mango is my fav fruit"
print(e[-17:-22:-2])
