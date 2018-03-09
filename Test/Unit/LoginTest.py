import sys, os

# Import for Windows
if os.name == 'nt':
	PathToUse = '..\..'
# Import for Linux
else:
	PathToUse = '../..'

sys.path.append( os.path.join( os.path.dirname( __file__ ), PathToUse, 'Login' ) )

import Login

## Run the Register Function
## The Player json files get written and created locally in the same folder

Login.Register()

