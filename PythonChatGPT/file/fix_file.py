def write_from_file(file):
	with open(file,"w") as file_name:
		file_name.write('5\n')
		file_name.write('Dung Lai\n')
		file_name.write('Linh Chi\n')
		file_name.write('Ngoc Anh\n')
		file_name.write('Duc Anh\n')
		file_name.write('Quynh Huong\n')

def read_from_file(file):
	with open(file,"r") as file_name:
		count = file_name.readline().strip()
		
		data = file_name.read().strip()
		rows = data.split("\n")

		print(f"Total students are: {count}")

		for i in range(len(rows)):
			print(f"Student {i+1}: {rows[i]}")


def main():
	file_name = "students.txt"
	write_from_file(file_name)
	read_from_file(file_name)
main()