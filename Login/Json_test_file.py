import json

student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}

json_data_file = json.dumps(student, indent=4)

with open("FlameWright.json", "w") as file:
   json.dump(json_data_file, file, indent=4)

with open("FlameWright.json", "r") as file:  
	student_info = json.load(file)
	
print(student_info)
