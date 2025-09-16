import pandas as pd

#read csv file into pandas DataFrame
data = pd.read_csv('data.csv', encoding='utf-8')

#display header (columns)
header = data.columns


# Course prices, dictionary
course_id_prices = {
    'A1': 799,
    'A2': 499,
    'A3': 749,
    'A4': 499,
    'A5': 999,
    'A6': 249,
    'A7': 149
}
# total_money = 0
# for i, student in data.iterrows(): #student is element in Pandas DataFrame
# 	course_id = student['course_id'] # i = course_id
# 	is_paid = student['is_paid'] # i = is_paid

# 	if is_paid == True:
# 		total_money += course_id_prices[course_id]

# print(total_money)

#------------------------------------------------------------------

# 	2 - Draw a piechart
import matplotlib.pyplot as plt
# courses_price = [0,0,0,0,0,0,0] #A1 A2 ... A7
# for i, student in data.iterrows(): #student is element in Pandas DataFrame
# 	course_id = student['course_id'] # i = course_id
# 	is_paid = student['is_paid'] # i = is_paid

# 	if is_paid == True:
# 		# course_id[1] is '1 in A1', - 1 equal to 1 
# 		courses_price[int(course_id[1]) - 1] += course_id_prices[course_id]
# print(courses_price)


# Simplified course labels for the pie chart
course_labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']

# Detailed course labels including names and prices for the legend
legend_labels = [
    "A1 Lập Trình Python Cơ Bản đến Nâng Cao (799k VND)",
    "A2 Logic Math – Toán Tư Duy Cơ Bản (499k VND)",
    "A3 Lập Trình Web Cơ Bản (749k VND)",
    "A4 AI – Trí Tuệ Nhân Tạo Cơ Bản (499k VND)",
    "A5 Python Excel – Tự Động Hoá (999k VND)",
    "A6 Data Science Cơ Bản (249k VND)",
    "A7 Lập Trình Game (149k VND)"
]

# Define the color palette to match the pie chart
colors = ['#e377c2', '#8c564b', '#9467bd', '#d62728', '#2ca02c', '#ff7f0e', '#1f77b4']

# # Create a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(courses_price, labels=course_labels, autopct='%1.1f%%', startangle=90, counterclock=False, colors=colors)

# # Title and legend
# plt.title('Distribution of Amounts for Each Course')
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# plt.legend(legend_labels, title="Legend", loc="upper left", bbox_to_anchor=(1, 1), fontsize='small', title_fontsize='medium')

# # Show the plot
# plt.tight_layout()  # Adjust the layout to make room for the legend
# plt.show()


#------------------------------------------------------------------

#draw barchart
# number_of_student_per_course = [0,0,0,0,0,0,0]
# for i, student in data.iterrows():
# 	course_id = student['course_id']
# 	is_paid = student['is_paid']

# 	if is_paid == True:
# 		number_of_student_per_course[int(course_id[1]) - 1] += 1
# print(number_of_student_per_course)


# # Create a bar chart
# plt.figure(figsize=(10, 6))
# bars = plt.bar(course_labels, number_of_student_per_course, color=colors, )  # Use the defined colors

# # Title and labels
# plt.title('Number of Paid Students per Course')
# plt.xlabel('Courses')
# plt.ylabel('Number of Students')

# # Set limits for the y-axis to ensure there's space above the bars
# plt.ylim(0, max(number_of_student_per_course) + 500)  # Add a bit of space above the highest bar

# # Add absolute numbers and percentage annotations to each bar
# total_paid_students = sum(number_of_student_per_course)
# for bar in bars:
#     height = bar.get_height()
#     percentage = (height / total_paid_students) * 100
#     # Display both absolute number and percentage
#     plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}\n({percentage:.1f}%)', 
#           ha='center', va='bottom')

# # Add legend for the bar chart
# # Create a proxy artist for each label to match the colors
# patches = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
# plt.legend(patches, legend_labels, title="Courses", loc="upper left", bbox_to_anchor=(0.5, 0.9), fontsize='small', title_fontsize='medium')

# # Remove the top and right spines (optional to make the plot look cleaner)
# ax = plt.gca()  # Get current axes
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# # Show the plot
# plt.tight_layout()  # Adjust layout to make room for the legend
# plt.show()

#-----------------------------------------------------------------


import matplotlib.ticker as ticker
#Create line chart
# Filter data for students who have paid
data_paid = data[data['is_paid'] == True].copy()

# Map course prices to the data
data_paid['price'] = data_paid['course_id'].map(course_id_prices)

# Convert 'payment_date' to datetime
data_paid['date'] = pd.to_datetime(data_paid['date'], format='%d/%m/%y', dayfirst=True)

# Group the data by year and month, then sum the revenue for each month
monthly_revenue = data_paid.groupby(data_paid['date'].dt.to_period('M'))['price'].sum()

# Convert the PeriodIndex to datetime objects that matplotlib can plot
monthly_revenue.index = monthly_revenue.index.to_timestamp()

# Increase figure size for better spacing
fig, ax = plt.subplots(figsize=(10, 6))

# Set limits for the y-axis to ensure there's space above the line
plt.ylim(0, max(monthly_revenue) + 100000)

# Plot the monthly revenue line chart
ax.plot(monthly_revenue.index, monthly_revenue.values, marker='o', color='b', markersize=8)

# Customize the chart
plt.title('Monthly Revenue from Paid Students', fontsize=18)
plt.xlabel('Month-Year', fontsize=14)
plt.ylabel('Revenue (VND)', fontsize=14)
plt.grid(True)

# Customize the x-axis labels to show (m/yy)
plt.xticks(ticks=monthly_revenue.index, labels=[d.strftime('%m/%y') for d in monthly_revenue.index], rotation=45, ha='right')

# Format y-axis with thousand separators and VND label
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,} VND'))

# Add annotations for each data point to show the exact revenue
for x, y in zip(monthly_revenue.index, monthly_revenue.values):
    ax.annotate(f'{int(y):,}', xy=(x, y), xytext=(0, 10), textcoords='offset points',
                ha='center', va='bottom', fontsize=9, color='red', fontweight='bold')

# Adjust layout manually to increase margins
plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.25)

plt.show()