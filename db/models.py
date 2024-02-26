from sqlalchemy import Column, Integer, String
from db.session import Base

class Peer(Base):
    __tablename__ = 'peer'
    id = Column(String, primary_key=True)
    id_network = Column(String, unique=True, index=True)

