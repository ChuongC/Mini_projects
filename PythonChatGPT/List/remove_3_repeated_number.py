numbers = [1,7,3,4,1,75,1,7,3,3]
remove_list = []

for i in range(len(numbers)):
	frequency = 0 #count =0
	for j in range(len(numbers)):
		if numbers[i] == numbers [j]:
			frequency += 1
	if frequency >= 3:
		remove_list.append(numbers[i])
for i in range(len(remove_list)):
	numbers.remove(remove_list[i])
print(numbers)