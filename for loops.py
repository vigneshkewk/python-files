#for loops = a statement that will execute its block of code for a limited amount of time
# while loop = unlimited
#for loop = limited



#for i in range(10):
    #print(i)

#for i in range(50,100): #or range(50,100+1) for printing 100 also
    #print(i)

#for i in range(50,100,2):
  #  print(i)

#by using for loops we can iterate strings
#for i in "vignesh atluri":
    #print(i)

#lets create a code that will print a mesasage when it count downs to zero
#for that we need to import time module
import time
for i in range(10,0,-1): # -1 means starts counting from 10 and ends at 0 +1 vice versa
    print(i)
    time.sleep(1)
print("happy new year")