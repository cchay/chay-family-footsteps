class Place:
	def __init__( self ):
		self.__ID = 0
		self.__Type = ''#Buildings are only available at places, Places is a map location 
		self.__Description = ''
		self.__Name = ''
		self.__CanHaveBuildings = False
		self.__Navigation = ''
	
	
	def GetID( self ):
		return self.__ID
	
	
	def SetID( self, Id ):
		self.__ID = Id	
	
	
	def GetType( self ):
		return self.__Type
	
	
	def GetType( self, Type ):
		self.__Type = Type
		
	
	def GetDescription( self ):
		return self.__Description
	
	
	def GetDescription( self, Id ):
		self.__ID = Id
	
	
	def GetName( self ):
		return self.__Name
	
	
	def GetName( self, name ):
		self.__Name = name
	
	
	def GetCanHaveBuildings( self ):
		return self.__ID
	
	
	def GetCanHaveBuildings( self, canhavebuildings ):
		self.__GetCanHaveBuildings = canhavebuildings
	
	
	def GetNavigation( self ):
		return self.__CanGoTo


	def SetNavigation( self, navigation ):
		self.__Navigation = navigation





class Town(Place):
	def __init__( self ):
#		self.__Type = 'Place'
#		self.__CanHaveBuildings = True
		self.__Inventory = []
		
	
	def Shop( self ):
		print('Welcome to the General Store!')
		
	
	def GetInventory( self ):
		return self.__Inventory
		#Todo, Need the Weapon, Armour and Thing json data files
	
		



















