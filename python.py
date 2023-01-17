import requests
import json

# Set up the API endpoint and access token
api_url = "https://api.box.com/2.0/files/"
access_token = "ASq8MSgjUuMrFSuoZ6f8OwxtMVnAwrSl"
# The ID of the file to be copied
file_id = "1113023725040"

# The ID of the parent folder where the copies will be created
parent_folder_id = "190182795566"

# Create a loop to copy the file 1000 times
for i in range(100):
    # Set up the data for the API request
    data = {
        "parent": {"id": parent_folder_id},
        "name": f"File1 {i+1}.xlsx"
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "As-User": "18199389449",
        "Content-Type": "application/json"
    }
    # Make the API request to copy the file
    response = requests.post(f"{api_url}{file_id}/copy", data=json.dumps(data), headers=headers)
    if response.status_code != 201:
        print(f"Error copying file: {response.json()}")
        break

print("All files copied successfully!")
