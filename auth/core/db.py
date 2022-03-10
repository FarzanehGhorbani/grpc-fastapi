from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient
from motor.core import AgnosticDatabase


class Mongo:
    db: AgnosticDatabase = None
    client: AgnosticClient = None

    @classmethod
    async def create_connection(cls, 
                                connection: str = "mongodb://root:example@192.168.63.26:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false",
                                database_name: str = "Authentication"):
        if cls.client is None:
            cls.client = AsyncIOMotorClient(connection)
            cls.db = cls.client[database_name]
