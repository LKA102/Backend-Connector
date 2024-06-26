import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

#Load environment variables from .env file
load_dotenv()

headers = {
        'Content_Type':'application/json',
        'Accept':'application/json',
        'Authorization':f"Token {os.getenv('TOKEN_API')}"
    }

def create_setupkey(name: str, datetime_created: datetime):
    payload = json.dumps({
        "name": f'{name}-{datetime_created}',
        "type": "one-off",
        "expires_in": 86400,
        "revoked": False,
        "auto_groups": [
            "cp193taknhds7393sog0"
        ],
        "usage_limit": 0,
        "ephemeral": True
    })
    with requests.Session() as client:
        response = client.post(f"{os.getenv('API_URI')}/api/setup-keys", headers=headers, data=payload)
        return response