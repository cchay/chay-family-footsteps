import sys, os

#Import for Windows
if os.name == 'nt':
	PathToUse = '..\..'
# Import for Linux
else:
	PathToUse = '../..'

sys.path.append(os.path.join(os.path.dirname(__file__), PathToUse, 'Classes'))

import Player

p = Player.Player().GetNewPlayer( 'Jane', '' )
p.ShowPlayerInfo()

print( "\n" )

p1 = Player.Player().GetNewPlayer( 'Thor', 'Ma' )
p1.ShowPlayerInfo()
