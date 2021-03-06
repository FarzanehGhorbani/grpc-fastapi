# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from auth.protos import user_pb2 as auth_dot_protos_dot_user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/UserService/GetUser',
                request_serializer=auth_dot_protos_dot_user__pb2.GetUserRequest.SerializeToString,
                response_deserializer=auth_dot_protos_dot_user__pb2.GetUserResponse.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/UserService/CreateUser',
                request_serializer=auth_dot_protos_dot_user__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=auth_dot_protos_dot_user__pb2.CreateUserResponse.FromString,
                )
        self.changePassowrd = channel.unary_unary(
                '/UserService/changePassowrd',
                request_serializer=auth_dot_protos_dot_user__pb2.changePassowrdRequest.SerializeToString,
                response_deserializer=auth_dot_protos_dot_user__pb2.GetUserResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def changePassowrd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=auth_dot_protos_dot_user__pb2.GetUserRequest.FromString,
                    response_serializer=auth_dot_protos_dot_user__pb2.GetUserResponse.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=auth_dot_protos_dot_user__pb2.CreateUserRequest.FromString,
                    response_serializer=auth_dot_protos_dot_user__pb2.CreateUserResponse.SerializeToString,
            ),
            'changePassowrd': grpc.unary_unary_rpc_method_handler(
                    servicer.changePassowrd,
                    request_deserializer=auth_dot_protos_dot_user__pb2.changePassowrdRequest.FromString,
                    response_serializer=auth_dot_protos_dot_user__pb2.GetUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/GetUser',
            auth_dot_protos_dot_user__pb2.GetUserRequest.SerializeToString,
            auth_dot_protos_dot_user__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/CreateUser',
            auth_dot_protos_dot_user__pb2.CreateUserRequest.SerializeToString,
            auth_dot_protos_dot_user__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def changePassowrd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/changePassowrd',
            auth_dot_protos_dot_user__pb2.changePassowrdRequest.SerializeToString,
            auth_dot_protos_dot_user__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
