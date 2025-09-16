
def main():

	apple_price = float(input('Enter the apple price:\n'))

	apple_quantity = int(input('Enter the apple quantity:\n'))

	print('Enter the meat price per gram:')
	meat_price = float(input())

	print('Enter the meat weight(in gram):')
	meat_weight = float(input())

	print('Enter your name:')
	name = input()

	#Total price
	total_price = str((meat_price*meat_weight)+(apple_price*apple_quantity))

	#print("Total bills for "+ name + "are $" +total_price+ ".")
	print_result = f"Total bills for {name} are ${total_price}." #f is string format
	print(print_result)
	
	#print("Items include " +str(apple_quantity)+ "and " +str(meat_weight)+ "gram of meat.")
	print("Items include {} and {} gram of meat.".format(apple_quantity,meat_weight))

main()


