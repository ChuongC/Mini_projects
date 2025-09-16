def read_integer_in_range(promt,min,max):
	while True:
		try:
			user_input = int(input(promt))
			if min <= user_input <=max :
				return user_input #End loop when return
			else:
				print(f"Input must be an integer between {min} and {max}")
		except ValueError:
			print("Invalid input. Please enter an integer.")
def level_menu():
	finished = False 
	while not finished:
		print("---------- Sub Menu ----------")
		print("--- 1. Level Easy          ---")
		print("--- 2. Level Hard          ---")
		print("--- 3. Return to Main Menu ---")
		print("------------------------------")
		choice = read_integer_in_range("Please enter your choice:", 1,3)

		if choice == 1:
			input("You select level easy. Press enter to play...")
		if choice == 2:
			input("You select level hard. Press enter to play...")
		if choice == 3:
			input("You select return to main menu. Press enter to continue...")
			finished = True

def view_dashboard():
	print("You select view dasboard. Press enter to continue...")

def main():
	finished = False
	while not finished:
		print("---------- Menu ---------")
		print("--- 1. Start playing  ---")
		print("--- 2. View dashboard ---")
		print("--- 3. Exit           ---")
		print("-------------------------")
		choice = read_integer_in_range("Please enter your choice:", 1,3)
		if choice == 1:
			level_menu()
		if choice == 2:
			view_dashboard()
		if choice == 3:
			input("\nGoodbye. Press enter to exit ...")			
			finished = True
		else:
			input("Please select again")
main()