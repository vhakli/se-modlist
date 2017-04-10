''' 
	This program will print you a list of mods that you 
	can easily paste to the dedicated server software
	You need a Steam Web API key from https://steamcommunity.com/dev/apikey
	This code does not take any inputs, you must hardcode the values below

	Created by Ville Häkli 2017
	https://ville.is
	ville@ville.is

	Licensed under GNU GPLv3
'''

import requests  
import json  
import sys

# Define variables
apikey = 'Insert web api key here' # You must acquire a key from https://steamcommunity.com/dev/apikey
workshop_collection_id = 'Insert workshop collection id here' # ID is found in the collection page url
output_file = 'Write preferred filename/path here' # e.g. 'modlist.txt'

# YOU DON'T HAVE TO EDIT BELOW THIS

# Define parameters for the POST-request 
payload = {'key': apikey,  
            'collectioncount': '1', 
            'publishedfileids[0]': workshop_collection_id}

# Send the POST-request with required data and load it to a variable
r = requests.post('https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/', data=payload)  
json_data = json.loads(r.text)

# Open a file in the same directory, empty it and set it to append mode for later use
f = open(output_file, 'w+')  
f.write('')  
f = open(output_file, 'a')

# Verify JSON data
if 'response' not in json_data or 'collectiondetails' not in json_data['response']:  
    print('Invalid JSON data')
    sys.exit(1)

# Go through the JSON data and output each line to the previously opened file
collectiondetails = json_data['response']['collectiondetails']  
for collectiondetail in collectiondetails:  
    for child in collectiondetail['children']:
        print(child['publishedfileid'])
        f.write(child['publishedfileid'])
        f.write('\n')
