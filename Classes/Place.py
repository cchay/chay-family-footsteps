#import sys, os
#sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', 'Data' ) )
import ThingClass

Thing = ThingClass.

class Place:
	def __init__( self ):
		self.__ID = 0
		self.__Type = ''#Buildings are only available at places, Places is a map location 
		self.__Description = ''
		self.__Name = ''
		self.__CanHaveBuildings = False
		self.__Navigation = []
	
	
	def GetID( self ):
		return self.__ID
	
	
	def SetID( self, Id ):
		self.__ID = Id	
	
	
	def GetType( self ):
		return self.__Type
	
	
	def SetType( self, Type ):
		self.__Type = Type
		
	
	def GetDescription( self ):
		return self.__Description
	
	
	def SetDescription( self, Description ):
		self.__Description = Description
	
	
	def GetName( self ):
		return self.__Name
	
	
	def SetName( self, Name ):
		self.__Name = Name
	
	
	def GetCanHaveBuildings( self ):
		return self.__CanHaveBuildings
	
	
	def SetCanHaveBuildings( self, CanHaveBuildings ):
		self.__CanHaveBuildings = CanHaveBuildings
	
	
	def GetNavigation( self ):
		return self.__Navigation


	def AddNavigation( self, Navigation ):
		self.__Navigation.append(Navigation)
	
	
	def RemoveNavigation( self, Navigation ):
		try:
			self.__Navigation.remove(Navigation)
		except:
			print('Navigation you listed is not on the list.')


class Town(Place):
	def __init__( self ):
#		self.__Type = 'Place'
#		self.__CanHaveBuildings = True
		self.__Inventory = []
		
	
	def Shop( self ):
		print('Welcome to the General Store!')
		# Thing: ID, Name, Type, Description, Weight, Price
		return '''ID: %i, Name: %s, Description: %s, Weight: %d, Price: $%d''' % ()
		
	
	def GetInventory( self ):
		return self.__Inventory
		#Todo, Need the Weapon, Armour and Thing json data files
	
		



















