numbers = [5,7,1,2,3,10,25]
print(f"Original number list {numbers}")

def find_largest_number(maximum):
	for i in range(len(numbers)):
		if numbers[i] > i+1:
			maximum = numbers[i]
	return maximum

largest = find_largest_number(numbers)
numbers.remove(largest)
print(f"Number list after removed the largest number {numbers}")
second_largest = find_largest_number(numbers)
print(f"The second largest number is {second_largest}")
