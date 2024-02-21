#nested loops = loop inside loop (the "inner loop" will finish all of its iteration before finishing the one iteration of the  outer loop
rows = int(input("how many rows do you want?: "))
coloumns = int(input("how many coloumns do you want?: "))
symbol = input("enter a symbol to use:")
for i in range(rows):
    for j in range(coloumns):
        print(symbol,end="")
    print()