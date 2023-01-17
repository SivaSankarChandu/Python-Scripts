import requests
import json

python script run through the postman to copy files in box cloud

import requests
import json

# Set the request parameters
url = 'https://api.box.com/2.0/files/content'

# Specify the file to be copied
file_id = '1113023725040'

# Set proper headers
headers = {'Authorization':'Bearer ASq8MSgjUuMrFSuoZ6f8OwxtMVnAwrSl',
           'Content-Type':'application/json'}

# Set the parameters
data={ "name": "filename_copy.txt",
       "parent": { "id": "190182795566" } }

# Do the HTTP post request
response = requests.post(url, data=json.dumps(data), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
