from pydantic import BaseModel
from datetime import datetime

class PeerBase(BaseModel):
    id: int

class PeerCreate(PeerBase):
    name: str

class SetupkeyCreate(BaseModel):
    id: int
    name: str
    datetime_created: datetime = datetime.now()