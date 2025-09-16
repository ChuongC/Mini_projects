import pandas as pd

# Sample data simulating `data_paid`
data = pd.DataFrame({
    'is_paid': [True, True, True, True, True],
    'course_id': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'date': ['01/02/23', '15/03/23', '25/04/23', '05/05/23', '15/06/23']
})

# Simulated course prices
course_id_prices = {
    'A1': 799000,
    'A2': 499000,
    'A3': 749000,
    'A4': 499000,
    'A5': 999000
}

# Filter data for students who have paid
data_paid = data[data['is_paid'] == True].copy()

# Map course prices to the data
data_paid['price'] = data_paid['course_id'].map(course_id_prices)

# Convert 'payment_date' to datetime
data_paid['date'] = pd.to_datetime(data_paid['date'], format='%d/%m/%y', dayfirst=True)

# Group the data by year and month, then sum the revenue for each month
monthly_revenue = data_paid.groupby(data_paid['date'].dt.to_period('M'))['price'].sum()

# Print the calculated monthly totals to verify correctness
print("Monthly revenue totals:")
print(monthly_revenue)
