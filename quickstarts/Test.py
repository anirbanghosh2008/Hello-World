import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [25, 35, 20, 20]  # Percentages
colors = ['gold', 'lightblue', 'lightgreen', 'coral']
explode = (0.1, 0, 0, 0)  # Highlight the first slice

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add a title
plt.title('Pie Chart Example')

# Display the chart
plt.show()
