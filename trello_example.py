import requests
from dotenv import load_dotenv
import os 
load_dotenv()

# Get all the boards

url = "https://api.trello.com/1/members/me/boards"

query = {
    "key": os.getenv('KEY'),
    "token": os.getenv('TOKEN')
}

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    params=query,
    headers=headers
)

# Response 
print("Boards:")

for i in response.json():
    print(i['name'])
parsed=response.json()[0] # This is the first board

# Uncomment to view complete response of the first board
#print(json.dumps(parsed, indent=2, sort_keys=True))

id=parsed['id']

# Url for the cards
url = f"https://api.trello.com/1/boards/{id}/cards"

response = requests.request(
    "GET",
    url,
    params=query,
    headers=headers
)

# Response
print("\nCards in first board:")

for i in response.json():
     print(i['name'])
