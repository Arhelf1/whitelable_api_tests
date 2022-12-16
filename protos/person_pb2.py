# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/common/person.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/common/person.proto',
  package='proto.common',
  syntax='proto3',
  serialized_options=_b('P\001\242\002\013ProtoCommon'),
  serialized_pb=_b('\n\x19proto/common/person.proto\x12\x0cproto.common\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf4\x01\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08lastname\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12,\n\x08\x62irthday\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x06gender\x18\x07 \x01(\x0e\x32\x1b.proto.common.Person.Gender\x12\r\n\x05login\x18\x08 \x01(\t\x12\x16\n\x0everified_phone\x18\n \x01(\t\"-\n\x06Gender\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\x08\n\x04MALE\x10\x02\x42\x10P\x01\xa2\x02\x0bProtoCommonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_PERSON_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='proto.common.Person.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=276,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_PERSON_GENDER)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='proto.common.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.common.Person.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.common.Person.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastname', full_name='proto.common.Person.lastname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='proto.common.Person.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birthday', full_name='proto.common.Person.birthday', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='proto.common.Person.gender', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login', full_name='proto.common.Person.login', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verified_phone', full_name='proto.common.Person.verified_phone', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERSON_GENDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=321,
)

_PERSON.fields_by_name['birthday'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PERSON.fields_by_name['gender'].enum_type = _PERSON_GENDER
_PERSON_GENDER.containing_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'proto.common.person_pb2'
  # @@protoc_insertion_point(class_scope:proto.common.Person)
  })
_sym_db.RegisterMessage(Person)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)