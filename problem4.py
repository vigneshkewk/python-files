#Iterate the given list of numbers and print only those numbers which are divisible by 5
list1 = [10,20,55,43,60]
print("given list is :", list1)
print("divisible by 5:")
for i in list1:
    if i % 5 == 0:
        print(i)