from bson.objectid import ObjectId as BsonObjectId
from pydantic import BaseModel

class ObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    @classmethod
    def validate(cls, v):
        try:
            if isinstance(v, BsonObjectId):
                return str(v)

            return BsonObjectId(str(v))
        except:
            raise ValueError("Not a valid ObjectId")


    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(example=str(BsonObjectId()))

    
class User(BaseModel):
    objectId:ObjectId
    name:str
    email:str
    password:str