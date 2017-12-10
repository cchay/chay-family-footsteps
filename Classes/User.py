import json
import os


class User:
	def __init__(self):
		self.Username = ''
		self.Password = ''
		self.FirstName = ''
		self.LastName = ''
	
	
	def getUsername(self):
		return self.Username
		
	def setUsername(self, name):
		self.Username = name
	
	
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
		filename = self.Username + '.json'
		return filename
	
	def __str__(self):
		return '''
Username: {}
Password: {}
First Name: {}
Last Name: {}
''' .format(self.Username, self.Password, self.FirstName, self.LastName)#Login().getUsername(), Login().getPassword(), Login().getFirstName(), Login().getLastName())
		
	def jsonDefault(self, object):
		return object.__dict__
