import sys, os

## Import for Windows
if os.name == 'nt':
	RelativePath = '..\..'

## Import for Linux
else:
	RelativePath = '../..'

sys.path.append( os.path.join( os.path.dirname( __file__ ), RelativePath, 'Classes' ) )	
sys.path.append( os.path.join( os.path.dirname( __file__ ), RelativePath, 'Engine' ) )
import Player
import Combat

p1 = Player.Player().GetNewPlayer( 'Donald Trump', 'Male' )
p1.ShowPlayerInfo()
print("\n")

p2 = Player.Player().GetNewPlayer( 'Kim Jung Un', 'Male' )
p2.ShowPlayerInfo()
print("\n")

print( "Fighters: ", p1.GetName(), "vs", p2.GetName() )
Combat.ResolveCombat( p1, p2 )
Loser = p1.GetName() if ( p1.GetCurrentHP() < p2.GetCurrentHP() ) else p2.GetName()
print ( Loser, "lost." )
