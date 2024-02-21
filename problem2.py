#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
print("printing numbers from 1 to 10")
previous_num = 0

for i in range(1,11):
    prev_current_sum = previous_num + i
    print("current number",i , "previous number", previous_num,"sum of these two is :",prev_current_sum)

    previous_num = i