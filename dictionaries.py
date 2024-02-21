#dictionary = a changeable, unordered collection of unique key:value pairs They are fast as they use hashing and allow us to access a value quickly they are also mutable
capitals = {'usa':'washington','india':'new delhi','china':'bejining','soviet union':'moscow'}
#print(capitals['soviet union']) # in dictionaries we donot use index values instead we use keys to acces its values
#print(capitals.get('india')) # another way to access an element
#print(capitals.keys())# used to print only keys
#print(capitals.values())#used to print only values
#print(capitals.items())#used to display entire dictionary
capitals.update({'germany':'berlin'}) # added new key value pairs
capitals.update({'india':'hyderabad'})# can change elementvalues of keys
capitals.pop('china')#pop is used to remove an key value pairs
#capitals.clear() # clears entire dictionary


for i in capitals.items():
    print(i)