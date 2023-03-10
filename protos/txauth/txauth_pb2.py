# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc/txauth/txauth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.txauth import session_pb2 as proto_dot_txauth_dot_session__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc/txauth/txauth.proto',
  package='grpc.txauth',
  syntax='proto3',
  serialized_options=_b('P\001\242\002\003FNM'),
  serialized_pb=_b('\n\x18grpc/txauth/txauth.proto\x12\x0bgrpc.txauth\x1a\x1aproto/txauth/session.proto\x1a\x17google/rpc/status.proto\"\xa4\x01\n\x11SessionKeyRequest\x12=\n\x08provider\x18\x01 \x01(\x0e\x32+.grpc.txauth.SessionKeyRequest.AuthProvider\x12\r\n\x05login\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"/\n\x0c\x41uthProvider\x12\x0b\n\x07TRANSAQ\x10\x00\x12\x08\n\x04\x45\x44OX\x10\x01\x12\x08\n\x04\x45TNA\x10\x02\"E\n\x12SessionKeyResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x1d\n\x0eSessionRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"j\n\x0fSessionResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x0b\n\x03key\x18\x02 \x01(\t\x12&\n\x07session\x18\x03 \x01(\x0b\x32\x15.proto.txauth.Session2\xa7\x01\n\x06TXAuth\x12R\n\rGetSessionKey\x12\x1e.grpc.txauth.SessionKeyRequest\x1a\x1f.grpc.txauth.SessionKeyResponse\"\x00\x12I\n\nGetSession\x12\x1b.grpc.txauth.SessionRequest\x1a\x1c.grpc.txauth.SessionResponse\"\x00\x42\x08P\x01\xa2\x02\x03\x46NMb\x06proto3')
  ,
  dependencies=[proto_dot_txauth_dot_session__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])



_SESSIONKEYREQUEST_AUTHPROVIDER = _descriptor.EnumDescriptor(
  name='AuthProvider',
  full_name='grpc.txauth.SessionKeyRequest.AuthProvider',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSAQ', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDOX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ETNA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=212,
  serialized_end=259,
)
_sym_db.RegisterEnumDescriptor(_SESSIONKEYREQUEST_AUTHPROVIDER)


_SESSIONKEYREQUEST = _descriptor.Descriptor(
  name='SessionKeyRequest',
  full_name='grpc.txauth.SessionKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='grpc.txauth.SessionKeyRequest.provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login', full_name='grpc.txauth.SessionKeyRequest.login', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='grpc.txauth.SessionKeyRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SESSIONKEYREQUEST_AUTHPROVIDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=259,
)


_SESSIONKEYRESPONSE = _descriptor.Descriptor(
  name='SessionKeyResponse',
  full_name='grpc.txauth.SessionKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.txauth.SessionKeyResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.txauth.SessionKeyResponse.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=330,
)


_SESSIONREQUEST = _descriptor.Descriptor(
  name='SessionRequest',
  full_name='grpc.txauth.SessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.txauth.SessionRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=332,
  serialized_end=361,
)


_SESSIONRESPONSE = _descriptor.Descriptor(
  name='SessionResponse',
  full_name='grpc.txauth.SessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.txauth.SessionResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='grpc.txauth.SessionResponse.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session', full_name='grpc.txauth.SessionResponse.session', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=363,
  serialized_end=469,
)

_SESSIONKEYREQUEST.fields_by_name['provider'].enum_type = _SESSIONKEYREQUEST_AUTHPROVIDER
_SESSIONKEYREQUEST_AUTHPROVIDER.containing_type = _SESSIONKEYREQUEST
_SESSIONKEYRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_SESSIONRESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_SESSIONRESPONSE.fields_by_name['session'].message_type = proto_dot_txauth_dot_session__pb2._SESSION
DESCRIPTOR.message_types_by_name['SessionKeyRequest'] = _SESSIONKEYREQUEST
DESCRIPTOR.message_types_by_name['SessionKeyResponse'] = _SESSIONKEYRESPONSE
DESCRIPTOR.message_types_by_name['SessionRequest'] = _SESSIONREQUEST
DESCRIPTOR.message_types_by_name['SessionResponse'] = _SESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionKeyRequest = _reflection.GeneratedProtocolMessageType('SessionKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONKEYREQUEST,
  '__module__' : 'grpc.txauth.txauth_pb2'
  # @@protoc_insertion_point(class_scope:grpc.txauth.SessionKeyRequest)
  })
_sym_db.RegisterMessage(SessionKeyRequest)

SessionKeyResponse = _reflection.GeneratedProtocolMessageType('SessionKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONKEYRESPONSE,
  '__module__' : 'grpc.txauth.txauth_pb2'
  # @@protoc_insertion_point(class_scope:grpc.txauth.SessionKeyResponse)
  })
_sym_db.RegisterMessage(SessionKeyResponse)

SessionRequest = _reflection.GeneratedProtocolMessageType('SessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONREQUEST,
  '__module__' : 'grpc.txauth.txauth_pb2'
  # @@protoc_insertion_point(class_scope:grpc.txauth.SessionRequest)
  })
_sym_db.RegisterMessage(SessionRequest)

SessionResponse = _reflection.GeneratedProtocolMessageType('SessionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRESPONSE,
  '__module__' : 'grpc.txauth.txauth_pb2'
  # @@protoc_insertion_point(class_scope:grpc.txauth.SessionResponse)
  })
_sym_db.RegisterMessage(SessionResponse)


DESCRIPTOR._options = None

_TXAUTH = _descriptor.ServiceDescriptor(
  name='TXAuth',
  full_name='grpc.txauth.TXAuth',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=472,
  serialized_end=639,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSessionKey',
    full_name='grpc.txauth.TXAuth.GetSessionKey',
    index=0,
    containing_service=None,
    input_type=_SESSIONKEYREQUEST,
    output_type=_SESSIONKEYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSession',
    full_name='grpc.txauth.TXAuth.GetSession',
    index=1,
    containing_service=None,
    input_type=_SESSIONREQUEST,
    output_type=_SESSIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TXAUTH)

DESCRIPTOR.services_by_name['TXAuth'] = _TXAUTH

# @@protoc_insertion_point(module_scope)
