from pydantic import BaseModel

class UserIncomeMode(BaseModel):
    name:str
    email:str
    password:str

    