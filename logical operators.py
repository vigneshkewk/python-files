#logical operators(and,or,not) = these are used to check if two or more conditional statements are true

temp = int(input("what is the temparature outside?:"))
if (temp >= 0 and temp <= 30):
    print("we can go outside its warm")
    print(("lets go outside"))
elif (temp<0 or temp>30):
    print("the temperature is bad today")
    print("stay indoors")
# here the not operator reverses it i.e if true it will make it false and vice versa
#if not(temp >= 0 and temp <= 30)
#elif not(temp<0 or temp>30)