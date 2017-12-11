import random

class Player():
	# Constructor
	def __init__( self ):
		# Private member vars; do not access directly; use getters and setters
		self.__Name = ''
		self.__Age = 0 # 18
		self.__Gender = '' # Male/Female
		
		# Normal human attribute is 1 (feeble) to 10 (olympian)
		self.__Strength = 0
		
		self.__Agility = 0
		self.__Constitution = 0
		self.__AttributePoints = 0
		
		# 1000/level
		self.__XP = 0
		
		# 1-10 levels
		self.__Level = 0

		# Normal human start with 1-100
		self.__HP = 0
		self.__CurrentHP = 0

		self.__DamageMod = 0
		self.__StrHitMod = 0
		self.__AgilityHitMod = 0
		self.__ACMod = 0
		self.__InitiativeMod = 0
		self.__HPMod = 0

		# naked 1-100 highest
		self.__AC = 0
		
		
	# Private Member Variable Getters & Setters
	def GetName( self ):
		return self.__Name
		
	def SetName( self, Name ):
		self.__Name = Name if ( Name != "" ) else "NoName"
	
	def GetAge( self ):
		return self.__Age
		
	def SetAge( self, Age ):
		self.__Age = Age
	
	def GetGender( self ):
		return self.__Gender
		
	def SetGender( self, Gender ):
		# Gender will be one of 4: Male, Female, Not Applicable, Unknown
		if ( Gender == "Male" or Gender == "Female" or Gender == "Not Applicable" ):
			self.__Gender = Gender
		else:
			self.__Gender = "Unknown"	
	
	def GetStrength( self ):
		return self.__Strength
		
	def SetStrength( self, Strength ):
		self.__Strength = Strength
	
	def GetAgility( self ):
		return self.__Agility
		
	def SetAgility( self, Agility ):
		self.__Agility = Agility
	
	def GetConstitution( self ):
		return self.__Constitution
		
	def SetConstitution( self, Constitution ):
		self.__Constitution = Constitution
	
	def GetAttributePoints( self ):
		return self.__AttributePoints
		
	def SetAttributePoints( self, AttributePoints ):
		self.__AttributePoints = AttributePoints

	def GetXP( self ):
		return self.__XP
		
	def SetXP( self, XP ):
		self.__XP = XP
	
	def GetLevel( self ):
		return self.__Level
		
	def SetLevel( self, Level ):
		self.__Level = Level
	
	def GetHP( self ):
		return self.__HP
		
	def SetHP( self, HP ):
		self.__HP = HP
	
	def GetCurrentHP( self ):
		return self.__CurrentHP
		
	def SetCurrentHP( self, CurrentHP ):
		self.__CurrentHP = CurrentHP
	
	def GetDamageMod( self ):
		return self.__DamageMod
		
	def SetDamageMod( self, DamageMod ):
		self.__DamageMod = DamageMod

	def GetStrHitMod( self ):
		return self.__StrHitMod
		
	def SetStrHitMod( self, StrHitMod ):
		self.__StrHitMod = StrHitMod

	def GetAgilityHitMod( self ):
		return self.__AgilityHitMod
		
	def SetAgilityHitMod( self, AgilityHitMod ):
		self.__AgilityHitMod = AgilityHitMod

	def GetACMod( self ):
		return self.__ACMod
		
	def SetACMod( self, ACMod ):
		self.__ACMod = ACMod

	def GetInitiativeMod( self ):
		return self.__InitiativeMod
		
	def SetInitiativeMod( self, InitiativeMod ):
		self.__InitiativeMod = InitiativeMod

	def GetHPMod( self ):
		return self.__HPMod
		
	def SetHPMod( self, HPMod ):
		self.__HPMod = HPMod

	def GetAC( self ):
		return self.__AC
		
	def SetAC( self, AC ):
		self.__AC = AC

	# Other methods
	def GetNewPlayer( self, Name, Gender ):
		self.SetName( Name )
		self.SetAge( 18 )
		self.SetGender( Gender )
		self.SetStrength( self.GenerateAttribute() )
		self.SetAgility( self.GenerateAttribute() )
		self.SetConstitution( self.GenerateAttribute() )
		self.SetAttributePoints( 3 )
		
		# attribute mod for gender
		if ( self.GetGender() == 'Male' and self.GetStrength() < 10 ):
			#print( "Strength Before:", self.GetStrength() )
			self.SetStrength( self.GetStrength() + 1 )
			#print( "Strength After:", self.GetStrength() )
		elif ( self.GetGender() == 'Female' and self.GetAgility() < 10 ):
			#print( "Agility Before:", self.GetAgility() )
			self.SetAgility( self.GetAgility() + 1 )
			#print( "Agility After:", self.GetAgility() )
			
		self.SetXP( 0 )
		self.SetLevel( 1 )
		self.SetDamageMod( self.GetAttributeMod( self.GetStrength() ) )
		self.SetStrHitMod( self.GetAttributeMod( self.GetStrength() ) )
		self.SetAgilityHitMod( self.GetAttributeMod( self.GetAgility() ) )
		self.SetACMod( self.GetAttributeMod( self.GetAgility() ) )
		self.SetInitiativeMod( self.GetAttributeMod( self.GetAgility() ) )
		self.SetHPMod( self.GetAttributeMod( self.GetConstitution() ) )
		self.SetHP( self.GenerateHP() )
		self.SetCurrentHP( self.GetHP() )
		self.SetAC( self.GenerateAC() )
		return self
		
	def GenerateAttribute( self ):
		return random.randint( 1, 10 )
	
	def GenerateHP( self ):
		x = random.randint( 1, 100 ) + self.GetHPMod()
		return x if ( x > 0 ) else 1
	
	def GenerateAC( self ):
		# Add armor bonus
		x = self.GetACMod()
		return x if ( x > 0 ) else 1
	
	def GetAttributeMod( self, Attribute ):
		if ( Attribute == 10 ):
			return 25
		if ( Attribute == 9 ):
			return 15
		if ( Attribute == 8 ):
			return 10
		if ( Attribute == 7 ):
			return 5
		if ( Attribute == 6 ):
			return 2
		if ( Attribute == 5 ):
			return 0
		if ( Attribute == 4 ):
			return -2
		if ( Attribute == 3 ):
			return -10
		if ( Attribute == 2 ):
			return -20
		if ( Attribute == 1 ):
			return -30
		

	def GotHurt( self ):
		#Todo
		pass

	def GotHealed( self ):
		#Todo
		pass
	
	def GotExperience( self ):
		#Todo
		pass

	def LeveledUp( self ):
		#Todo
		self.SetAttributePoints( self.SetAttributePoints() + 3 )
		
	# debugging
	def ShowPlayerInfo( self ):
		print( "Name: ", self.GetName() )
		print( "Age: ", self.GetAge() )
		print( "Gender: ", self.GetGender() )
		print( "Strength: ", self.GetStrength() )
		print( "Agility: ", self.GetAgility() )
		print( "Constitution: ", self.GetConstitution() )
		print( "XP: ", self.GetXP() )
		print( "AttributePoints: ", self.GetAttributePoints() )
		print( "Level: ", self.GetLevel() )
		print( "HP: ", self.GetHP() )
		print( "Current HP: ", self.GetCurrentHP() )
		print( "DamageMod: ", self.GetDamageMod() )
		print( "StrHitMod: ", self.GetStrHitMod() )
		print( "AgilityHitMod: ", self.GetAgilityHitMod() )
		print( "ACMod: ", self.GetACMod() )
		print( "InitiativeMod: ", self.GetInitiativeMod() )
		print( "HPMod: ", self.GetHPMod() )
		print( "AC: ", self.GetAC() )
