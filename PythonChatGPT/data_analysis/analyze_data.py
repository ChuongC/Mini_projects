import pandas as pd

file = "data.csv"
data = pd.read_csv(file)

# display the first few rows of dataset to inspect its structure
header = data.head()

# Course prices, dictionary
course_prices = {
    'A1': 799,
    'A2': 499,
    'A3': 749,
    'A4': 499,
    'A5': 999,
    'A6': 249,
    'A7': 149
}

#filter the data to include only paid students
data_paid = data[data['is_paid']].copy()

data_paid['price'] = data_paid['course_id'].map(course_prices)

fee_per_student = data_paid['price']

#calculate the total money
total_money_collected = fee_per_student.sum() * 1000
print(total_money_collected)


import matplotlib.pyplot as plt
# Pie chart
#Group by 'course_id' and count number of paid students
money_per_course = data_paid.groupby('course_id')['price'].sum()

#Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(money_per_course, labels=money_per_course.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Percentage of total money collected per course')
plt.axis('equal') # Equal aspect ratio ensures the pie is drawn as a circle.
plt.show()


#Group by 'coure_id' and count number of students per course (paid and unpaid)
students_per_course = data.groupby('course_id')['Id'].count()


#Plotting the bar chart
plt.figure(figsize=(10,6))
students_per_course.plot(kind='bar', color = 'skyblue', edgecolor='black')
plt.title("Number of students Enrolled in each course")
plt.xlabel('Course ID')
plt.ylabel('Number of students')
plt.xticks(rotation=0)
plt.show()


#create a line chart showing monthly revenue for each year
data_paid['date'] = pd.to_datetime(data_paid['date'], format='%d/%m/%y')

# Extract the month and year from the date
data_paid['year_month'] = data_paid['date'].dt.to_period('M')

monthly_revenue = data_paid.groupby('year_month')['price'].sum()

#Plotting the line chart
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line',marker='o',color='green')
plt.title('Monthly revenue over time')
plt.xlabel('Month-Year')
plt.ylabel('Revenue: ')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#Age Distribution Analysis
# Extract the ages of all registered students
ages = data['age']

# Plotting a histogram to show the distribution of ages
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages of Registered Students')
plt.xlabel('Age')
plt.ylabel('Number of Students')
plt.grid(True)
plt.show()

# Alternatively, we can also use a boxplot to visualize the age distribution
plt.figure(figsize=(8, 6))
plt.boxplot(ages, vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Boxplot of Student Ages')
plt.xlabel('Age')
plt.grid(True)
plt.show()
