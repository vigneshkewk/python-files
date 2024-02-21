def first_last_same(numberlist):
    print("given list is:",numberlist)
    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
number_x = [10,20,30,30,10]
print("the result is :",first_last_same(number_x))

number_y = [65,56,78,56,45,32]
print("the result",first_last_same(number_y))