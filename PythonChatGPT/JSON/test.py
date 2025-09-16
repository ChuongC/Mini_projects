import json

my_dict = {"name":"Chuong", "age":22}
my_dict["male"] = True
my_dict["family_member"] = ["Lam, Mom, Dad"]
with open("test.json","w") as file:
	json.dump(my_dict, file, indent = 4)