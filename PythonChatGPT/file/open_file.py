with open("data.txt","w") as file:
	file.write("Cao Van Chuong\n")
	file.write("Learning\n")
	file.write("12\n")
	file.write("34\n")


with open("data.txt","r") as file:
	
	data = file.read()
	row = data.split("\n")[:-1]

	for i in range(len(row)):
		print(row[i])

with open("data.txt","a") as file:
	data = file.write("Don't fear to be wrong")

with open("data.txt","r") as file:
	new_row = file.read()
	print(new_row)