# json
import json
data = '''{
	"name" : "Chuck",
	"phone:" {
	"type" : "intl",
	"number" : "+1 73315487"
	},
	"email" : {
	"hide" : "yes"
	}
}'''
info = json.loads(data) # the info will be a python dictionary or a nested list(a list containing many dictionaries)
print('name:',info["name"]) 
#>>> return Chuck
print('hide:',info["email"]["hide"])
#>>> return yes