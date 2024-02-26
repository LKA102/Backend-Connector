import httpx
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

headers = {
        'Accept':'application/json',
        'Authorization':f"Token {os.getenv('TOKEN_API')}"
    }

async def get_peer_network(id_network: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{os.getenv('API_URI')}/api/peers/{id_network}", headers=headers)
        return response
    
async def get_all_peers():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{os.getenv('API_URI')}/api/peers", headers=headers)
        return response
    

