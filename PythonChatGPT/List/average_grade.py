import csv


# Your row as a string
row = 'Cao Van Chuong,"4,6","6,5","3,9",21'

# Use csv.reader to parse the row
reader = csv.reader([row])

# Extract the values from the parsed row
parsed_row = next(reader)

name = parsed_row[0]

numberic_values = parsed_row[1:-1]

numbers = [float(num.replace(',','.'))for num in numberic_values]
print(numbers)
if numbers:
	average = sum(numbers)/len(numbers)
print(name)
print(round(average,2))