import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Classes'))
import Player

sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Engine'))
import Combat

p1 = Player.Player().GetNewPlayer( 'Jane', 'Female' )
p1.ShowPlayerInfo()

p2 = Player.Player().GetNewPlayer( 'Jack', 'Male' )
p2.ShowPlayerInfo()

Combat.ResolveCombat( p1, p2 )