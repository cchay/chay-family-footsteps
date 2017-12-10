import random

def ResolveCombat( Creature1, Creature2 ):
	print( "Begin combat!\n")
	while ( Creature1.GetCurrentHP() > 0 and Creature2.GetCurrentHP() > 0 ):
		print( "Fight!", Creature1.GetCurrentHP(), Creature2.GetCurrentHP(), "\n" )
		# Resolve Createture1's attack
		if ( GetHitRoll() >= Creature2.GetAC() ):
			Creature2.SetCurrentHP( Creature2.GetCurrentHP() - Creature1.GetStrength() )

		# Resolve Createture2's attack
		if ( GetHitRoll() >= Creature1.GetAC() ):
			Creature1.SetCurrentHP( Creature1.GetCurrentHP() - Creature2.GetStrength() )
	
def GetHitRoll():
	return random.randint( 1, 100 )