# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/txauth/txauth_provider.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/txauth/txauth_provider.proto',
  package='proto.txauth',
  syntax='proto3',
  serialized_options=_b('P\001\242\002\003FNM'),
  serialized_pb=_b('\n\"proto/txauth/txauth_provider.proto\x12\x0cproto.txauth\"\x84\x01\n\x0c\x41uthProvider\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10userflow_enabled\x18\x02 \x01(\x08\x12\x14\n\x0ctfa_required\x18\x03 \x01(\x08\x12\x14\n\x0cpin_required\x18\x04 \x01(\x08\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x12\n\nis_private\x18\x06 \x01(\x08\x42\x08P\x01\xa2\x02\x03\x46NMb\x06proto3')
)




_AUTHPROVIDER = _descriptor.Descriptor(
  name='AuthProvider',
  full_name='proto.txauth.AuthProvider',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.txauth.AuthProvider.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userflow_enabled', full_name='proto.txauth.AuthProvider.userflow_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tfa_required', full_name='proto.txauth.AuthProvider.tfa_required', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pin_required', full_name='proto.txauth.AuthProvider.pin_required', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.txauth.AuthProvider.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_private', full_name='proto.txauth.AuthProvider.is_private', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=53,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['AuthProvider'] = _AUTHPROVIDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthProvider = _reflection.GeneratedProtocolMessageType('AuthProvider', (_message.Message,), {
  'DESCRIPTOR' : _AUTHPROVIDER,
  '__module__' : 'proto.txauth.txauth_provider_pb2'
  # @@protoc_insertion_point(class_scope:proto.txauth.AuthProvider)
  })
_sym_db.RegisterMessage(AuthProvider)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
