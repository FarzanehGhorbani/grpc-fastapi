# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth/protos/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61uth/protos/user.proto\"P\n\x15\x63hangePassowrdRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x13\n\x0boldPassword\x18\x02 \x01(\t\x12\x13\n\x0bnewPassword\x18\x03 \x01(\t\"\x1f\n\x0eGetUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"!\n\x0fGetUserResponse\x12\x0e\n\x06status\x18\x02 \x01(\x05\"B\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\"\n\x12\x43reateUserResponse\x12\x0c\n\x04name\x18\x04 \x01(\t2\xb4\x01\n\x0bUserService\x12.\n\x07GetUser\x12\x0f.GetUserRequest\x1a\x10.GetUserResponse\"\x00\x12\x37\n\nCreateUser\x12\x12.CreateUserRequest\x1a\x13.CreateUserResponse\"\x00\x12<\n\x0e\x63hangePassowrd\x12\x16.changePassowrdRequest\x1a\x10.GetUserResponse\"\x00\x62\x06proto3')



_CHANGEPASSOWRDREQUEST = DESCRIPTOR.message_types_by_name['changePassowrdRequest']
_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetUserResponse']
_CREATEUSERREQUEST = DESCRIPTOR.message_types_by_name['CreateUserRequest']
_CREATEUSERRESPONSE = DESCRIPTOR.message_types_by_name['CreateUserResponse']
changePassowrdRequest = _reflection.GeneratedProtocolMessageType('changePassowrdRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEPASSOWRDREQUEST,
  '__module__' : 'auth.protos.user_pb2'
  # @@protoc_insertion_point(class_scope:changePassowrdRequest)
  })
_sym_db.RegisterMessage(changePassowrdRequest)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'auth.protos.user_pb2'
  # @@protoc_insertion_point(class_scope:GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'auth.protos.user_pb2'
  # @@protoc_insertion_point(class_scope:GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'auth.protos.user_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'auth.protos.user_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHANGEPASSOWRDREQUEST._serialized_start=26
  _CHANGEPASSOWRDREQUEST._serialized_end=106
  _GETUSERREQUEST._serialized_start=108
  _GETUSERREQUEST._serialized_end=139
  _GETUSERRESPONSE._serialized_start=141
  _GETUSERRESPONSE._serialized_end=174
  _CREATEUSERREQUEST._serialized_start=176
  _CREATEUSERREQUEST._serialized_end=242
  _CREATEUSERRESPONSE._serialized_start=244
  _CREATEUSERRESPONSE._serialized_end=278
  _USERSERVICE._serialized_start=281
  _USERSERVICE._serialized_end=461
# @@protoc_insertion_point(module_scope)
