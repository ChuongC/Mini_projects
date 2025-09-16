# Read an integer between min and max, prompting with the string provided
def read_integer_in_range(prompt, minimum, maximum):
  while True:
    try:
      user_input = int(input(prompt))
      if minimum <= user_input <= maximum:
        return user_input
      else:
        print(f"Input must be an integer between {minimum} and {maximum}.")
    except ValueError:
      print("Invalid input. Please enter an integer.")

def level_menu():
  # complete this code to support the menu options below - use the main menu code to guide you.
  print("---------- Sub Menu ----------")
  print("--- 1. Level Easy          ---")
  print("--- 2. Level Hard          ---")
  print("--- 3. Return to Main Menu ---")
  print("------------------------------")
  choice = read_integer_in_range("Please enter your choice:", 1, 3)

def view_dashboard():
  input("You select view dashboard. Press enter to continue...")

def main():
  finished = False
  while not finished:
    print("---------- Menu ---------")
    print("--- 1. Start playing  ---")
    print("--- 2. View dashboard ---")
    print("--- 3. Exit           ---")
    print("-------------------------")
    choice = read_integer_in_range("Please enter your choice: ", 1, 3)
    if choice == 1: 
      level_menu()
    elif choice == 2:
      view_dashboard()
    elif choice == 3:
      finished = True
    else:
      input("Please select again")

main()