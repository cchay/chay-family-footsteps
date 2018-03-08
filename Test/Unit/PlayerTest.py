import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..', 'Classes'))
import Player

p = Player.Player().GetNewPlayer( 'Jane', '' )
p.ShowPlayerInfo()

print( "\n" )

p1 = Player.Player().GetNewPlayer( 'Thor', 'Ma' )
p1.ShowPlayerInfo()
