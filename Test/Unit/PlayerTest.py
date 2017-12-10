import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Classes'))
import Player

p = Player.Player().GetNewPlayer( 'Wonder Woman', 'Female' )
p.ShowPlayerInfo()

print( "\n" )

p1 = Player.Player().GetNewPlayer( 'Superman', 'Male' )
p1.ShowPlayerInfo()
