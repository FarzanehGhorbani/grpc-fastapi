from . import router
from ..app.grpc_client import create_user ,get_user
from fastapi import Response

@router.post("/")
async def sign_up(user:dict):
    try:
        result = await create_user(user)
        return Response(status_code=200,content=result)
    except TypeError as e:
        return Response(status_code=200,content=f'{e}')


@router.get("/")
async def login(user:dict):
    try:
        result = await get_user(user)
        if result.status:
            return Response(status_code=200,content='Login')
        else:
            return Response(status_code=200,content='you shoutl authenticated')
    except TypeError as e:
        return Response(status_code=200,content=f'{e}')