from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from db.session import get_db
from db.crud import *
from db.schemas import PeerCreate
from api_calls import peer_api
router = APIRouter()

@router.get("/api/peers/{id}")
async def retrieve_peer(id: str, db:Session = Depends(get_db)):
    db_peer = get_peer(db=db, peer_id=id)
    if not db_peer:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND, detail="Peer does not exist"
       )
    response = peer_api.get_peer_network(db_peer.id_network)
    return Response(response.content, response.status_code, response.headers)


@router.get("/api/peers")
async def list_peers():
    response = peer_api.get_all_peers()
    return Response(response.content, response.status_code, response.headers)

@router.post("/api/peers")
async def save_peer(peer: PeerCreate, db:Session = Depends(get_db)):
    response_peers = peer_api.get_all_peers()
    if response_peers.status_code != 200:
        raise HTTPException(
            #Si hay error, fijars en la api de netbird (El error que mando aqui es generico)
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error"
        )
    peers_list = response_peers.json()
    new_peer = next(filter(lambda obj: obj['hostname'] == peer.name, peers_list)) #Filtramos el peer por el hostname
    if not new_peer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Peer not found"
        )
    new_peer_db = get_peer(db=db, peer_id=peer.id)
    if new_peer_db:
        update_peer(db=db, peer=new_peer_db, network_id=new_peer['id'])
    else:
        create_peer(db=db, peer=peer, network_id=new_peer['id'])
    return new_peer


    
    






    

