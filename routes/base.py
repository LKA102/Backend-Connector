from fastapi import APIRouter
from routes.apiRoutes import peerRouter, setupkeyRouter

apiRouter = APIRouter()
apiRouter.include_router(peerRouter.router, prefix="", tags=["peers"])
apiRouter.include_router(setupkeyRouter.router, prefix="", tags=["setup-keys"])