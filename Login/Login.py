import json
import demjson
import os


## Converting Json data to Python 
#jsonData = {"name": "FlameWright", "password": "password"}
#jsonToPython = load(jsonData)

#print(jsonToPython)
#print(jsonToPython['name'])

## Converting Python dictionary to Json data

#pythonDictionary = {"name": "Nidan", "password": "sino"}
#dictionaryToJson = dumps(pythonDictionary)



#print(pythonDictionary)

class Login:
	def __init__(self):
		self.UserName = ''
		self.Password = ''
		self.FirstName = ''
		self.LastName = ''
	
	def getUserName(self):
		return self.UserName
		
	def setUserName(self, name):
		self.UserName = name
		
	def writeUserFileName(self):
		filename = self.UserName + '.json'
		return filename
		
def jsonDefault(object):
	return object.__dict__


FlameWright = Login()
FlameWright.setUserName("FlameWright")
file = open(str(FlameWright.writeUserFileName()), 'w+')#FlameWright.writeUserFileName(), 'w+')

print(FlameWright.writeUserFileName())
print(FlameWright.getUserName())


#print(abder, default=jsonDefault)
data = json.dumps(FlameWright, default=jsonDefault)

with open("FlameWright.json", "w") as file:
   json.dump(data, file, indent=4)

#print(data)
#data = demjson.encode(FlameWright)
#print(data)


#with open("FlameWright.json") as data:
#    result = data.read()

#print (type(result))
#print (result.keys())
#print (result)

#json.loads('FlameWright.json')
#profiles = pickle.load(open('profiles.pickle', 'rb'))























