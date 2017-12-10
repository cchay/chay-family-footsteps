import json, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Classes'))
import User

with open ('Me.json', 'r') as userfile:
	user_data = json.load(userfile)

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Data/User'))



with open ('Chris.json', 'r') as userfile:
	user_data = json.load(userfile)

usershell = User.User()


#pathOfUser = '../Class'
#pathForUserData = '../Data/User'


def login():
	#sys.path.append(os.path.abspath("../Data/User/"))
	#print ("Item exists: " + str(os.path.exists("Chris.json")))
	#print ("Item's path and name: " + str(os.path.split(os.path.realpath("Chris.json"))))
	print('Login:')
	username = input('Username: ')
	user_file_name = username + '.json'
	print(user_file_name)
	try:
		with open (user_file_name, 'r') as userfile:
			user_data = json.load(userfile)
	except FileNotFoundError as e:
		print('Wrong Username!!')
		return login()
		
		
	password = input('Password: ')
	
	
def register():
	pass


'''
   def login(self):
      print('Login Page')
      profile_name = input('Name: ') # Get the name the user types in
      if profile_name == 'b': # Checks to see if the user wants to go back
         return login().opening()
         
      password = input('Password: ')# Get the name the user types in
      if password == 'b': # Checks to see if the user wants to go back
         return login().opening()

      for i in profiles: # Goes through data to confirm user name
         if profile_name in profiles:
            if password == profiles[profile_name]['Password']:
               time.sleep(0.5)
               print('\n...Welcome, {profile}...' .format(profile = profile_name))
               time.sleep(1)
               profile.name = profile_name
               profile.password = password
               break
            else:
               print('The name or password was incorrect.')
               print('Type "b" in the password or profile name area if you want to back to the main page.')
               input('Press <ENTER> to continue')
               print('\n\n')
               return login().login()
         
         else:
            print('The name or password was incorrect.')
            print('Type "b" in the password or profile name area if you want to back to the main page.')
            input('Press <ENTER> to continue')
            print('\n\n')
            return login().login()
            


   def create(self):
      print('Sign up Page')
      new_profile = input('New Username: ')
      if new_profile == 'b':
         return login().opening()
      
      new_password = input('New Password: ')
      if new_password == 'b':
         return login().opening()
      

      if new_profile != '' and new_password != '':
         if not new_profile in profiles:
            print('Are you satisfied with Profile name: {}, and Profile password: {} ?' .format(new_profile, new_password))
            confirm = input('(y/n) ')
            if confirm == 'y':
               profiles[new_profile] = {'Password': new_password, 'Tasks': {}}
               profile.name = new_profile
               profile.password = new_password
               print('Profile successfully created! Welcome {}' .format(profile.name))
               input('Press <ENTER> to continue')
            else:
               return login().create()
         else:
            print('ERROR: Profile name already exists!')
            print('Type "b" in the password or profile name area if you want to back to the main page.')
            input('Press <ENTER> to continue')
            print('\n\n')
            return login().create()
      else:
         print('ERROR: You failed to fill out one of the forms.')
         print('Type "b" in the password or profile name area if you want to back to the main page.')
         input('Press <ENTER> to continue')
         print('\n\n')
         return login().create()
         



'''

'''
# Create empty shell for new user
user = Login()
#change Username to 'Chris'
user.setUserName('Chris')
print(user)

#Converts User_data to Dictionary form
user_data = user.jsonDefault(user)
print(user_data)

#Generates a file name based on the user's Username
user_data_filename = user.writeUserFileName()


with open(user_data_filename, "w") as file:
   json.dump(user_data, file, indent=4)

with open(user_data_filename, "r") as file:  
	user_data = json.load(file)

print(user_data)
print(user_data['UserName'])
user.setPassword('password')
user_data = user.jsonDefault(user)
print(user_data)

with open(user_data_filename, "w") as file:
   json.dump(user_data, file, indent=4)

'''


login()








