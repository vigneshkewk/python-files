#slicing = create a substring by extracting elements from another string
# indexing[] or slicing()
# [start:stop:step]
name = "senju kawaragi"
firstname = name[:5]
print(firstname) # or name[0:5]
lastname = name[6:] # or name[6:14]
print(lastname)
# step is used to print ever7y 2nd element  by default we have one
funkyname = name[0:14:2] # or name[::2] python assumes first empty dot a 0 index and nextr one as last index
print(funkyname)
monkename = name[0:14:3] # or name[::3]
print(monkename)
reversedname= name[::-1]
print(reversedname)
#slice function(used to create a slice function)

website1 = "http://google.com" #here let us remove and create  as string lets remove http and .com
slice1 = slice(7,-4,) #same as indexing but seperate with comma
print(website1[slice1])
website2 = "http://coding ninjas.com"
slice2 = slice(7,-4)
print(website2[slice2])

