import random

class Player():
	# Constructor
	def __init__( self ):
		# Private member vars; do not access directly; use getters and setters
		self._Name = ''
		self._Age = 0 # 18
		self._Gender = '' # Male/Female
		
		# Normal human attribute is 1 (feeble) to 10 (olympian)
		self._Strength = 0
		
		self._Agility = 0
		self._Constitution = 0
		self._AttributePoints = 0
		
		# 1000/level
		self._XP = 0
		
		# 1-10 levels
		self._Level = 0

		# Normal human start with 1-100
		self._HP = 0
		self._CurrentHP = 0

		self._DamageMod = 0
		self._StrHitMod = 0
		self._AgilityHitMod = 0
		self._ACMod = 0
		self._InitiativeMod = 0
		self._HPMod = 0

		# naked 1-100 highest
		self._AC = 0
		
		
	# Private Member Variable Getters & Setters
	def GetName( self ):
		return self._Name
		
	def SetName( self, Name ):
		self._Name = Name
	
	def GetAge( self ):
		return self._Age
		
	def SetAge( self, Age ):
		self._Age = Age
	
	def GetGender( self ):
		return self._Gender
		
	def SetGender( self, Gender ):
		self._Gender = Gender
	
	def GetStrength( self ):
		return self._Strength
		
	def SetStrength( self, Strength ):
		self._Strength = Strength
	
	def GetAgility( self ):
		return self._Agility
		
	def SetAgility( self, Agility ):
		self._Agility = Agility
	
	def GetConstitution( self ):
		return self._Constitution
		
	def SetConstitution( self, Constitution ):
		self._Constitution = Constitution
	
	def GetAttributePoints( self ):
		return self._AttributePoints
		
	def SetAttributePoints( self, AttributePoints ):
		self._AttributePoints = AttributePoints

	def GetXP( self ):
		return self._XP
		
	def SetXP( self, XP ):
		self._XP = XP
	
	def GetLevel( self ):
		return self._Level
		
	def SetLevel( self, Level ):
		self._Level = Level
	
	def GetHP( self ):
		return self._HP
		
	def SetHP( self, HP ):
		self._HP = HP
	
	def GetCurrentHP( self ):
		return self._CurrentHP
		
	def SetCurrentHP( self, CurrentHP ):
		self._CurrentHP = CurrentHP
	
	def GetDamageMod( self ):
		return self._DamageMod
		
	def SetDamageMod( self, DamageMod ):
		self._DamageMod = DamageMod

	def GetStrHitMod( self ):
		return self._StrHitMod
		
	def SetStrHitMod( self, StrHitMod ):
		self._StrHitMod = StrHitMod

	def GetAgilityHitMod( self ):
		return self._AgilityHitMod
		
	def SetAgilityHitMod( self, AgilityHitMod ):
		self._AgilityHitMod = AgilityHitMod

	def GetACMod( self ):
		return self._ACMod
		
	def SetACMod( self, ACMod ):
		self._ACMod = ACMod

	def GetInitiativeMod( self ):
		return self._InitiativeMod
		
	def SetInitiativeMod( self, InitiativeMod ):
		self._InitiativeMod = InitiativeMod

	def GetHPMod( self ):
		return self._HPMod
		
	def SetHPMod( self, HPMod ):
		self._HPMod = HPMod

	def GetAC( self ):
		return self._AC
		
	def SetAC( self, AC ):
		self._AC = AC

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
		print ( "Name: ", self.GetName() )
		print ( "Age: ", self.GetAge() )
		print ( "Gender: ", self.GetGender() )
		print ( "Strength: ", self.GetStrength() )
		print ( "Agility: ", self.GetAgility() )
		print ( "Constitution: ", self.GetConstitution() )
		print ( "XP: ", self.GetXP() )
		print ( "AttributePoints: ", self.GetAttributePoints() )
		print ( "Level: ", self.GetLevel() )
		print ( "HP: ", self.GetHP() )
		print ( "Current HP: ", self.GetCurrentHP() )
		print ( "DamageMod: ", self.GetDamageMod() )
		print ( "StrHitMod: ", self.GetStrHitMod() )
		print ( "AgilityHitMod: ", self.GetAgilityHitMod() )
		print ( "ACMod: ", self.GetACMod() )
		print ( "InitiativeMod: ", self.GetInitiativeMod() )
		print ( "HPMod: ", self.GetHPMod() )
		print ( "AC: ", self.GetAC() )
