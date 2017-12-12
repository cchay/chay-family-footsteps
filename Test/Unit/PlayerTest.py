import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..\..', 'Classes'))
import Player

<<<<<<< HEAD
p = Player.Player().GetNewPlayer( '', 'ALIEN')
=======
p = Player.Player().GetNewPlayer( 'Jane', 'Not Applicable' )
>>>>>>> master
p.ShowPlayerInfo()

print( "\n" )

<<<<<<< HEAD
p1 = Player.Player().GetNewPlayer( '', 'ALIEN!!' )
=======
p1 = Player.Player().GetNewPlayer( 'Thor', 'Ma' )
>>>>>>> master
p1.ShowPlayerInfo()
