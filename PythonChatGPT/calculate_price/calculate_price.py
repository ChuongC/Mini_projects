# Complete the three missing lines of code below

def main():
	apple_price = float(input('Enter the apple price:\n')) # assignment statement, naming convention, lower-case, newline character
	apple_quantity = int(input('Enter the apple quantity:\n')) 

	# complete the code below using apple price above as an example then uncomment the line:
	print('Enter the meat price per gram:')
	meat_price = float(input()) 

	print('Enter the meat weight (in gram):')
	meat_weight =  float(input())

	print('Enter your name:')
	name = input()

	# Calculate the total price:
	total_price = apple_price * apple_quantity + meat_price * meat_weight

	# Print the bill to the terminal in the following format:
	# Total bills for Dung Lai Lap Trinh are $285.51.
	# Items include 3 apples and 23.1 gram of meat.
	# print("Total bills for " + name + " are $" + str(total_price) + ".") 
	print(f"Total bills for {name} are ${total_price}.")
	# print("Items include " + str(apple_quantity) + " apples and " + str(meat_weight) + " gram of meat.")
	print("Items include {} apples and {} gram of meat.".format(apple_quantity, meat_weight))

main()

