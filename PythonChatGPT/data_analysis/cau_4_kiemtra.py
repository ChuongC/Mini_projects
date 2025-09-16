file = open("data.csv", "r", encoding="utf-8")
students = file.read().split("\n")[1:-1]
# Testing
# print(students[-1].split(",")[3])
# print(students[-1].split(",")[4])

total_earning_0224 = 0 
for s in students:
	# s = "35992,Trần Văn Trang,54,A1,04/06/23,True"
	s_row = s.split(",")
	# s_row = ["35992","Trần Văn Trang","54","A1","04/06/23","True"]
	date = s_row[4] # "04/06/23"
	date_YY_MM = s_row[4][3:]
	course_id = s_row[3]
	is_paid = s_row[5]
	if is_paid == "True" and date_YY_MM == "02/24":
		if course_id == "A1":
			total_earning_0224 += 799

		if course_id == "A2":
			total_earning_0224 += 499

		if course_id == "A3":
			total_earning_0224 += 749

		if course_id == "A4":
			total_earning_0224 += 499

		if course_id == "A5":
			total_earning_0224 += 999

		if course_id == "A6":
			total_earning_0224 += 249

		if course_id == "A7":
			total_earning_0224 += 149
print(total_earning_0224)