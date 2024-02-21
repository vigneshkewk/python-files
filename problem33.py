#Write a program to accept a string from the user and display characters that are present at an even index number.
word = input('enter a word')
print("original string:", word)

size = len(word)

print("printing only even index characters")
for i in range(0,size,2):
    print(i,word[i])
    