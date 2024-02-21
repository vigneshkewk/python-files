#loop control statements = change a loops execution from its normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#ex for break
#while True:
 #   name = input("enter your name?: ")
  #  if name != "":
       # break

#ex for continue
phone_no = "123-456-789"
#for i in phone_no:
  #  if i == "-": #here in o/p - betwwen ph no is removed
  #      continue
  #  print(i,end="")

#ex for pass
for i in range(1,21):
    if i == 13: #here it skipped 13
        pass
    else:
        print(i)