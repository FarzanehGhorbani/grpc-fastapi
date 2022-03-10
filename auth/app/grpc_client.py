from ..protos import user_pb2,user_pb2_grpc
import grpc
import logging
from google.protobuf.struct_pb2 import Struct
from fastapi import Response

async def client(kwargs):
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        s=Struct()
        s.update(kwargs)
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = await stub.CreateUser(user_pb2.CreateUserRequest(s))
        print(response)
        return response
        

async def create_user(user):
    exists_user=await get_user(user)
    if exists_user.status:
        return 'User already exists'

    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        await stub.CreateUser(user_pb2.CreateUserRequest(name=user['name'],email=user['email'],password=user['password']))
        
        return 'User created'
    


async def get_user(user):
    try:
        async with grpc.aio.insecure_channel('localhost:50051') as channel:
            stub=user_pb2_grpc.UserServiceStub(channel)
            response=await stub.GetUser(user_pb2.GetUserRequest(email=user['email']))
            return response
    except TypeError as e:
        raise e
    










