from sqlalchemy.orm import Session
from db import models, schemas

def get_peer(db: Session, peer_id: int):
    return db.query(models.Peer).filter(models.Peer.id == peer_id).first()

def create_peer(db:Session, peer: schemas.PeerCreate, network_id: str):
    db_peer = models.Peer(id=peer.id, id_network=network_id)
    db.add(db_peer)
    db.commit()
    db.refresh(db_peer)
    return db_peer

def update_peer(db:Session, peer: models.Peer, network_id: str):
    peer.id_network = network_id
    db.add(peer)
    db.commit()
    db.refresh(peer)
    return peer
