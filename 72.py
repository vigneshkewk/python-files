import matplotlib.pyplot as plt
x_days = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]
y_price2 = [11,12,10.5,11.5,12.5]

#defining the chart elemetns
plt.title('stock movment')
plt.xlabel('week days')
plt.ylabel('price in usd')
#function for plotting is "plot", lets see
plt.plot(x_days,y_price1,label ='stock1') 
plt.plot(x_days,y_price2,label = 'stock2')
#lets create the LEGENDS for these two stocks
plt.legend(loc=1,fontsize=12)
#finally to show plot
plt.show()