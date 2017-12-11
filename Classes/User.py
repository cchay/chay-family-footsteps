import json
import os


class User:
	def __init__( self ):
		self.__Username = ''
		self.__Password = ''
		self.__FirstName = ''
		self.__LastName = ''
	
	
	def getUsername( self ):
		return self.__Username
		
	def setUsername( self, name ):
		self.__Username = name
	
	
	def getPassword( self ):
		return self.__Password
		
	def setPassword( self, password ):
		self.__Password = password
	
	
	def getFirstName( self ):
		return self.__FirstName
		
	def setFirstName( self, name ):
		self.__FirstName = name
	
	
	def getLastName( self ):
		return self.__LastName
		
	def setLastName( self, name ):
		self.__LastName = name
		
		
	def writeUserFileName( self ):
		filename = self.__Username + '.json'
		return filename
	
	def __str__( self ):
		return '''
Username: {}
Password: {}
First Name: {}
Last Name: {}
''' .format( self.__Username, self.__Password, self.__FirstName, self.__LastName )#Login().getUsername(), Login().getPassword(), Login().getFirstName(), Login().getLastName())
		
	def jsonDefault( self, object ):
		return object.__dict__
