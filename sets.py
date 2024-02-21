# set = is an collection which is unordered and unindexed. no duplicate values
names = {"a","b","c"}
#names.add("d")
#names.remove("b")
#names.clear()
schools = {"vignan","kv","silver oaks"}
#names.update(schools)
#student = names.union(schools)
#print(names.difference(schools))#will print any different elements from both sets
print(schools.intersection(names))


for i in schools:
    print(i)
