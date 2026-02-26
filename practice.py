student = {
    "name": "Udhayaa",
    "age": 22,
    "course": "MCA"
}

print(student["name"])
print(student.get("age"))

student["city"] = "Chennai"     # Adding
student["age"] = 23                 # Updating

print(student.get("city"))
print(student["age"])

for key in student.values():
    print(key)

