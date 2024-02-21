#tuple = collection which is ordered and unchangeble used to group together related data
student = ("vig",21,"male")
print(student.count("vig"))
print(student.index("male"))

for i in student:
    print(i)
if "vig" in student:
    print("vig is here")