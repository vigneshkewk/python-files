#bar chat plotting
import matplotlib.pyplot as plt
x_cities = ['new york','london','dubai','newdelhi','tokyo']
y_temp = [75,65,105,98,90]
#define chart elemetns
plt.title('temperatures of cit''ies')
plt.xlabel('cities')
plt.ylabel('temp')
#plotting bar
plt.bar(x_cities,y_temp,)
plt.show()