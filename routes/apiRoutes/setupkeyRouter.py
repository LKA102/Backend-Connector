from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from api_calls import setupkey_api
from db.schemas import SetupkeyCreate

router = APIRouter()

@router.post("/api/setup-keys")
async def create_setupkey(setupkey: SetupkeyCreate):
    response = setupkey_api.create_setupkey(name=setupkey.name, datetime_created=setupkey.datetime_created)
    return Response(response.content,response.status_code,response.headers)



