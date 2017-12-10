class Place:
	def __init__(self):
		self.ID = 0
		self.Type = ''#Buildings are only available at places, Places is a map location 
		self.Description = ''
		self.Name = ''
		self.CanHaveBuildings = False
	
	def GetID(self):
		return self.ID
	
	def SetID(self, Id):
		self.ID = Id
	
	
	def GetType(self):
		return self.Type
	
	def GetType(self, Type):
		self.Type = Type
		
	
	def GetDescription(self):
		return self.Description
	
	def GetDescription(self, Id):
		self.ID = Id
	
	
	def GetName(self):
		return self.Name
	
	def GetName(self, name):
		self.Name = name
	
	
	def GetCanHaveBuildings(self):
		return self.ID
	
	def GetCanHaveBuildings(self, canhavebuildings):
		self.GetCanHaveBuildings = canhavebuildings





class Town(Place):
	def __init__(self):
		self.CanGoTo = ''
	
	def GetCanGoTo(self):
		return self.CanGoTo

	def SetCanGoTo(self, cangoto):
		self.CanGoTo = cangoto


















