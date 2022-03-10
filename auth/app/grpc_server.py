import grpc
import logging
from ..protos import user_pb2,user_pb2_grpc
from ..core.db import Mongo

class UserService(user_pb2_grpc.UserServiceServicer):
    async def CreateUser(self, request, context):
        logging.info("CreateUser")
        await Mongo.db['auth'].insert_one({'email':request.email,'name':request.name,'password':request.password})
        return user_pb2.CreateUserResponse(name=request.name)


    async def GetUser(self,request,context):
        logging.info("GetUser")
        user=await Mongo.db['auth'].find_one({'email':request.email})
        return user_pb2.GetUserResponse(status=1 if user else 0)
    
    async def changePassowrd(self, request, context):
        user=await Mongo.db['auth'].update_one({'email':request.email},{'$set':{'password':request.password}})
        return user_pb2.GetUserResponse(status=1)


async def serve():
    server=grpc.aio.server()
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(),server)
    server.add_insecure_port('[::]:50051')
    print('Starting server......')
    await server.start()
    await server.wait_for_termination()

















