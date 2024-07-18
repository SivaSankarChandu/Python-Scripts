import requests 
import json 

# Input Data 

box_access_token = "Enter the access token here" 
src_files = ["file1", "file2", "file3"] 
dst_folder_id = "Enter the destination folder id here" 

# API Call 

headers = { 
    "Authorization": "Bearer " + box_access_token 
} 

for src_file in src_files: 
    payload = { 
        "parent": { "id": dst_folder_id }, 
        "name": src_file 
    } 
    response = requests.post("https://api.box.com/2.0/files/content", headers=headers, data=json.dumps(payload)) 
    print(response.status_code)
