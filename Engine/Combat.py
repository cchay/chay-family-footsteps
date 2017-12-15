import random, time

def ResolveCombat( Creature1, Creature2 ):
	print( "Combat encounter!\n")
	print( "\n", Creature1.GetName(), "'s HP:", Creature1.GetCurrentHP(), "|||", Creature2.GetName(), "'s HP:", Creature2.GetCurrentHP(), "\n Press a button to continue ..." )
	input()
	Round = 1
	while ( Creature1.CanFight() == True and Creature2.CanFight() == True ):
		print( "\n Round", Round, "\n Press a button to fight!" )
		
		# Resolve Createture1's attack
		if ( GetHitRoll( Creature1 ) >= Creature2.GetAC() ):
			Damage = Creature1.GetStrength() + random.randint( 1,10 )
			Creature2.GotHurt( Damage )
			print( "\t", Creature1.GetName(), "hits", Creature2.GetName(), "for %i" % Damage )
		else: print( "\t", Creature1.GetName(), "missed." )
		
		# Resolve Createture2's attack
		if ( GetHitRoll( Creature2 ) >= Creature1.GetAC() ):
			Damage = Creature2.GetStrength() + random.randint( 1,10 )
			Creature1.GotHurt( Damage )
			print( "\t", Creature2.GetName(), "hits", Creature1.GetName(), "for %i" % Damage )
		else: print( "\t", Creature2.GetName(), "missed." )
		
		print( "\n", Creature1.GetName() + "'s HP:", Creature1.GetCurrentHP(), "|||", Creature2.GetName() + "'s HP:", Creature2.GetCurrentHP(), "\n" )
		Round += 1
		if ( Creature1.CanFight() == False or Creature2.CanFight() == False ): break
		print( "-" * 50 )
		#time.sleep( 1 )
		
def GetHitRoll( Creature1 ):
	HitRoll = Creature1.GetStrHitMod() + Creature1.GetAgilityHitMod() + random.randint( 1, 100 )
	HitRoll = HitRoll if ( HitRoll > 1 ) else 1
	return HitRoll