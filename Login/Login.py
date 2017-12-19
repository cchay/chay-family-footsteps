import json, sys, os

sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', 'Classes' ) )
import User

#sys.path.append( os.path.join( os.path.dirname( __file__ ), '..', 'Data', 'User' ) )
path = os.path.join( os.path.dirname( __file__ ), '..', 'Data', 'User' ) 
os.chdir( path )

usershell = User.User()

def Login():
	global usershell
	print( 'Login:' )
	username = input( 'Username: ' )
	user_file_name = username + '.json'
	try:
		with open ( user_file_name, 'r' ) as userfile:
			user_data = json.load( userfile )
	except FileNotFoundError as e:
		print( 'Wrong Username!!' )
		return Login()
	
	usershell.setUsername( user_data['_User__Username'] )
	usershell.setPassword( user_data['_User__Password'] )
	usershell.setFirstName( user_data['_User__FirstName'] )
	usershell.setLastName( user_data['_User__LastName'] )
		
		
	password = input( 'Password: ' )
	if password == usershell.getPassword():
		print( 'Correct! Welcome %s.' % usershell.getUsername() )
	else:
		return Login()
	
	
def Register():
	global usershell
	print( 'Registration:' )
	username = input( 'What do you want your Username to be? ' )
	password = input( 'Type your password: ' )
	firstname = input( 'Type your first name: ' )
	lastname = input( 'Type your last name: ' )
	
	usershell.setUsername( username )
	usershell.setPassword( password )
	usershell.setFirstName( firstname )
	usershell.setLastName( lastname )
	#Debugging: print(str(os.path.exists(usershell.writeUserFileName())))

	
	print( usershell )
	answer = input( 'Are you satisfied with this? ( y / n ): ' )
	if answer == 'n':
		return Register()
		
	else:
	
		if os.path.exists( usershell.writeUserFileName() ) == True:
			print( 'Username already exsists!' )
			return Register()
			
		elif not usershell.getUsername() or not usershell.getPassword():
				print( 'There cannot be any spaces in the Username or Password!' )
				return Register()	
			
		else:
			print( 'Welcome, %s!' % usershell.getUsername() )
	
	userfilename = usershell.writeUserFileName()
	userdata = usershell.jsonDefault( usershell )
	
	#Debugging: print('User Data:', userdata)
	
	
	with open( userfilename, 'w' ) as userfile:
		json.dump( userdata, userfile, indent=4 )
		
	return Login()








