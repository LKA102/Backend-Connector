from pydantic import BaseModel
from datetime import datetime

class PeerBase(BaseModel):
    id: str

class PeerCreate(PeerBase):
    name: str

class SetupkeyCreate(BaseModel):
    name: str
    datetime_created: datetime = datetime.now()