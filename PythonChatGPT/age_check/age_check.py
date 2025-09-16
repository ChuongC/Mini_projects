#Validate var

#age
while True:
	age = int(input('Enter your age (from 1 to 200):\n'))
	if (age >= 1) and (age <=200):
		break
	else:
		print("Make sure enter age from 1 to 200!, please try again")

# #voucher
# while True:
# 	voucher = input("Have voucher (yes or no):\n").strip().lower()
# 	if (voucher == "yes") or (voucher == "no" ):
# 		break
# 	else:
# 		print("Please try again (yes or no):\n")

#or validate voucher could be like
valid_voucher = False
has_voucher = False
while not valid_voucher:
	voucher = input("Have voucher (yes or no):\n").strip().lower()
	if voucher == "yes":
		#it will exit loop when valid_voucher not false
		valid_voucher = True
		has_voucher = True
	elif voucher == "no":
		valid_voucher = True
		has_voucher = False
	else:
		print("Please try again (yes or no):\n")


#check_age
is_child = False
is_adult = False
is_elder = False

if age < 18:
	is_child = True
elif age < 59:
	is_adult = True
else:
	is_elder = True

#check whether discount
discount = 0

if (is_child or is_elder) and (has_voucher): #for child and elder
	discount = 0.2

if (is_child or is_elder) and (not has_voucher):
	discount = 0.15

if (is_adult) and has_voucher: #for adult
	discount = 0.1

#Total amount of price
original_price = 649000 # Constant variable
discounted_price = original_price * (1-discount)

print(f"You got discount {int(discount*100)}%, total price is {discounted_price:.0f} VND.")

