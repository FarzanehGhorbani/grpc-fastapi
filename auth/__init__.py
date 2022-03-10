from .app.grpc_server import serve
from fastapi import FastAPI,Request
from .core.db import Mongo
import asyncio
# jwt_manager: JWT = JWT(secret="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", algorithm="HS256")
# bcrypt = CryptContext(schemes=["bcrypt"])


def create_app(config: dict = None) -> FastAPI:
    app = FastAPI()
    

    from .api import router
    
    @app.on_event("startup")
    async def startup():
        await Mongo.create_connection()
        loop=asyncio.get_event_loop()
        loop.create_task(serve())

        
    app.include_router(router)
    
    return app