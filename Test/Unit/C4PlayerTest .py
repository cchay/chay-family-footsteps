import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Classes'))
import Player


p2 = Player.Player().GetNewPlayer( '', '')
p2.ShowPlayerInfo()

print( "\n" )

p1 = Player.Player().GetNewPlayer( '', '' )
p1.ShowPlayerInfo()
