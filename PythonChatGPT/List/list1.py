numbers = [5,7,1,2,3,10,25]

# find the smallest function
def find_smallest(numbers):
	minimum = numbers[0]
	for index in range(len(numbers)):
		if numbers[index] < minimum:
			minimum = numbers[index]
	return minimum

# find the largest function
def find_largest(maximum):
	maximum = numbers[0]
	for index in range(len(numbers)):
		if numbers[index] > maximum:
			maximum = numbers[index]
	return maximum

# def find_theSecond_Largest(second):

def main():
	numbers = [5,7,1,2,3,10,25]
	print(numbers)

	result_min = find_smallest(numbers)
	result_max = find_largest(numbers)

	print(f"The smallest number is : {result_min}")
	print(f"The largest number is : {result_max}")

main()

