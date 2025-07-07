#chart in python 
#module matplotlib 
#pip install matplotlib
import matplotlib.pyplot as plt
#Line plot
plt.plot([1,2,3],[2,4,6])
plt.title("Line plot chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show() 

#bar chart
label=["A","B","C","D","E"]
sales=[100,200,500,400,700]
plt.bar(label,sales,color="blue")
plt.title("Sales report")
plt.ylabel("Values of sales")
plt.xlabel("Brands")
plt.show()

#pie chart
label=["A","B","C"]
sizes=[120,100,150]
plt.pie(sizes,labels=label,autopct="%1.1f%%",startangle=90)
plt.title("Product pie report")
plt.show()

#histogram chart
ages=[22,43,12,56,30]
gender=['m','f','m','f','f']
plt.hist(ages,bins=2,color="green",edgecolor="red")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()