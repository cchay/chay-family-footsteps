import sys, os

# Import for Windows
if os.name == 'nt':
	PathToUse = '../..'
# Import for Linux
else:
	PathToUse = '..\..'

sys.path.append( os.path.join( os.path.dirname( __file__ ), PathToUse, 'Classes'))
sys.path.append( os.path.join( os.path.dirname( __file__ ), PathToUse, 'Engine'))

import Player
import Combat

sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Engine'))
import Combat

p1 = Player.Player().GetNewPlayer( 'Jane', 'Female' )
p1.SetStatus( 'Dead' )
p1.ShowPlayerInfo()

p2 = Player.Player().GetNewPlayer( 'Jack', 'Male' )
p2.ShowPlayerInfo()

Combat.ResolveCombat( p1, p2 )
p1.ShowPlayerInfo()
p2.ShowPlayerInfo()
