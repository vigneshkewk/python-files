#creating histogram
import matplotlib.pyplot as plt
f = open('agedata75.csv','r')

agefile = f.readlines()
#we know that pyplot only accepts lists and arrays as an input so we need to convert this record(agedata75) in to list
age_list = []

for records in agefile:
    age_list.append(int(records))
    
bins = [0,10,20,30,40,50,60,70,80,90,100]

#plotting the histogram
plt.title('age histogram')
plt.xlabel('group')
plt.ylabel('age')
plt.hist(age_list,bins,histtype='bar',rwidth=0.9)
plt.show()