import random

class Player():
	# Constructor
	def __init__( self ):
		self._Name = ''
		self._Age = 0 # 18
		self._Gender = '' # Male/Female
		
		# Normal human attribute is 1 (feeble) to 10 (olympian)
		self._Strength = 0
		self._Agility = 0
		self._Constitution = 0
		
		# 1000/level
		self._XP = 0

		# 1-10 levels
		self._Level = 0

		# Normal human start with 1-100
		self._HP = 0

		# naked 0-10 highest
		self._AC = 0
		
		
	# Private Member Variable Getters & Setters
	def GetName(self):
		return self._Name
		
	def SetName(self, Name):
		self._Name = Name
	
	def GetAge(self):
		return self._Age
		
	def SetAge(self, Age):
		self._Age = Age
	
	def GetGender(self):
		return self._Gender
		
	def SetGender(self, Gender):
		self._Gender = Gender
	
	def GetStrength(self):
		return self._Strength
		
	def SetStrength(self, Strength):
		self._Strength = Strength
	
	def GetAgility(self):
		return self._Agility
		
	def SetAgility(self, Agility):
		self._Agility = Agility
	
	def GetConstitution(self):
		return self._Constitution
		
	def SetConstitution(self, Constitution):
		self._Constitution = Constitution
	
	def GetXP(self):
		return self._XP
		
	def SetXP(self, XP):
		self._XP = XP
	
	def GetLevel(self):
		return self._Level
		
	def SetLevel(self, Level):
		self._Level = Level
	
	def GetHP(self):
		return self._HP
		
	def SetHP(self, HP):
		self._HP = HP
	
	def GetAC(self):
		return self._AC
		
	def SetAC(self, AC):
		self._AC = AC

	# Other methods
	def GetRandomPlayer( self, Name, Gender ):
		self.SetName( Name )
		self.SetAge( 18 )
		self.SetGender( Gender )
#		self.SetStrength( self.GenerateAttribute() )
#		self.SetAgility( self.GenerateAttribute() )
#		self.SetConstitution( self.GenerateAttribute() )
		self.SetXP( 1 )
		self.SetLevel( 1 )
#		self.SetHP( self.GenerateHP() )
		self.SetAC( 1 )
		return self
		
	def GenerateAttribute( self ):
		return random.randint( 1, 10 )
	
	def GenerateHP( self ):
		return random.randint( 1, 100 )
	

p2 = Player().GetRandomPlayer( 'Jack', 'Male' )
print ( p2.GetAge() )
print ( p2.GetName() )