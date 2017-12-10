import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Classes'))
import Player

p = Player.Player().GetNewPlayer( '', 'FemaleFemale' )
p.ShowPlayerInfo()

print( "\n" )

p1 = Player.Player().GetNewPlayer( '', 'MaleMale' )
p1.ShowPlayerInfo()
