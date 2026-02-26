#DICTIONARY

'''
        - Key value pair
        - Mutable- value, key-Immutable
        - Ordered
        - Unindexed
        - Allows Duplicates(Only Values not keys)

       a={"key":"value"}
'''
#-------------------------------------------------------------------------------------------
'''
a={"name":"Akash",
     16:"age"}   #16- key: age- value
b=a

print(b,"\n")
print(a[16])       #Output : age

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)
'''
#-------------------------------------------------------------------------------------------
'''
a={"name" :input("Enter Name: "),
     "age":int(input("Enter Age: "))}
print(a)

print(a["name"],a["age"])
'''

'''
a={input("Enter key: "):"Udhayaa",
     input("Enter key2: "):22}
print(a)
'''

#1.get()----------------------------------------------------------------------------------
'''
a={"Apple":80,"Orange":70,"Cherry":60}
print(a.get("Orange"))

b=a.get("Banana",50)
print(b)
print(a)

b=a.setdefault("Banana",50)
print(b)
print(a)
'''

#2.clear------------------------------------------------------------------------------------
'''
a={"key":"Hello"}
b=a.copy()
print(b)

a={"key":"Hello"}
b=a
b.clear()
print(b)

'''
#-------------------------------------------------------------------------------------------
'''
marks={
    "maths":75,
    "science":44,
    "english":60,
    }

for i in marks:
    if marks[i]>=50:
        print(i,"- Pass")
    else:
        print(i,"- Fail")
'''


'''
attendance={
    "Arun":85,
    "Kumar":45
    }

for student in attendance:
    if attendance[student]>=75:
        print(student," - Allowed For Exam")
    else:
        print(student,"-Not Allowed")
'''

#3.items 4.keys 5.values 6.pop 7.popitem 8.update--------------------------------------------------------------------
'''
a={"color":"Black","name":"Red","brand":"A1"}
print(a.items())
print(a.keys())
print(a.values())

a.update({"color":"yellow:"})
print(a)
a["color"]="Green"
print(a)

a.popitem()
a.pop("name")
print(a)
a.reverse()
print(a)

'''











#Nested Dictionary-------------------------------------------------------------------------------------------
'''
a={"class1":{"name":"Udhayaa","age":22,"roll_no":3},
     "class2":{"name":"Balaji","age":23,"roll_no":4}}

print(a["class1"])
print(a["class1"]["name"])
print(a["class1"]["age"])

print(a["class2"]["name"],"\n\n\n\n")

for i in a:
    print(i)
    for j in a[i]:
        print(j,a[i][j])
'''
#-------------------------------------------------------------------------------------------
'''
users={
    1001:{"name":"Ravi","pin":1111,"balance":5000},
    1002:{"name":"Arun","pin":2222,"balance":7000},
    1003:{"name":"Kumar","pin":3333,"balance":3000},
    1004:{"name":"Ajith","pin":4444,"balance":9000},
    1005:{"name":"Vijay","pin":5555,"balance":6000}
    }

acc_no=int(input("Enter Account Number: "))
pin=int(input("Enter PIN: "))
withdraw=int(input("Enter Withdraw Amount: "))

if acc_no in users:
    if users[acc_no]["pin"]==pin:
        if withdraw<=users[acc_no]["balance"]:
            users[acc_no]["balance"]=users[acc_no]["balance"]-withdraw

            print("Withdraw Successful")
            print("Name:",users[acc_no]["name"])
            print("Remaining Balance: ",users[acc_no]["balance"])

        else:
            print("Insufficient Balance")            
    else:
        print("Wrong PIN")
else:
    print("Invalid Acc No.")

'''
#-------------------------------------------------------------------------------------------

users={
    1001:{"name":"Ravi","pin":1111,"balance":5000},
    1002:{"name":"Arun","pin":2222,"balance":7000},
    1003:{"name":"Kumar","pin":3333,"balance":3000},
    1004:{"name":"Ajith","pin":4444,"balance":9000},
    1005:{"name":"Vijay","pin":5555,"balance":6000}
    }

users.update({1006:{"name":"Udhayaa","pin":6666,"balance":8000}})
##users.update({int(input("Acc No.: ")):{"name:"

acc_no=int(input("Enter Account Number: "))
pin=int(input("Enter PIN: "))
withdraw=int(input("Enter Withdraw Amount: "))

if acc_no in users:
    if users[acc_no]["pin"]==pin:
        if withdraw<=users[acc_no]["balance"]:
            users[acc_no]["balance"]=users[acc_no]["balance"]-withdraw

            print("Withdraw Successful")
            print("Name:",users[acc_no]["name"])
            print("Remaining Balance: ",users[acc_no]["balance"])

        else:
            print("Insufficient Balance")            
    else:
        print("Wrong PIN")
else:
    print("Invalid Acc No.")

#new user add pannanum using setdefault method -Task
    # 3 option add pannanum
    # 1.new user add panurathu,
    # 2.existing user- balance enquiry ,withdraw

























