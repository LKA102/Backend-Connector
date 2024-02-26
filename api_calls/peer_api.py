import requests
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

headers = {
        'Accept':'application/json',
        'Authorization':f"Token {os.getenv('TOKEN_API')}"
    }

def get_peer_network(id_network: str):
    with requests.Session() as client:
        response = client.get(f"{os.getenv('API_URI')}/api/peers/{id_network}", headers=headers)
        return response
    
def get_all_peers():
    with requests.Session() as client:
        response = client.get(f"{os.getenv('API_URI')}/api/peers", headers=headers)
        return response
    

