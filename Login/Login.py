import json
import os


class User:
	def __init__(self):
		self.UserName = ''
		self.Password = ''
		self.FirstName = ''
		self.LastName = ''
	
	
	def getUserName(self):
		return self.UserName
		
	def setUserName(self, name):
		self.UserName = name
	
	
	def getPassword(self):
		return self.Password
		
	def setPassword(self, password):
		self.Password = password
	
	
	def getFirstName(self):
		return self.FirstName
		
	def setFirstName(self, name):
		self.FirstName = name
	
	
	def getLastName(self):
		return self.LastName
		
	def setLastName(self, name):
		self.LastName = name
		
		
	def writeUserFileName(self):
		filename = '/home/iceman/_/code/chay-family-footsteps/Data/User/' + self.UserName + '.json'
		return filename
	
	def __str__(self):
		return '''
Username: {}
Password: {}
First Name: {}
Last Name: {}
''' .format(self.UserName, self.Password, self.FirstName, self.LastName)#Login().getUserName(), Login().getPassword(), Login().getFirstName(), Login().getLastName())
		
	def jsonDefault(self, object):
		return object.__dict__


# Create empty shell for new user
user = Login()
#change Username to 'Chris'
user.setUserName('Chris')
print(user)

#Converts User_data to Dictionary form
user_data = user.jsonDefault(user)
print(user_data)

#Generates a file name based on the user's Username
user_data_filename = user.writeUserFileName()


with open(user_data_filename, "w") as file:
   json.dump(user_data, file, indent=4)

with open(user_data_filename, "r") as file:  
	user_data = json.load(file)

print(user_data)
print(user_data['UserName'])
user.setPassword('password')
user_data = user.jsonDefault(user)
print(user_data)

with open(user_data_filename, "w") as file:
   json.dump(user_data, file, indent=4)













