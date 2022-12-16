# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/common/tariff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.txauth import types_pb2 as proto_dot_common_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/common/tariff.proto',
  package='proto.common',
  syntax='proto3',
  serialized_options=_b('P\001\242\002\013ProtoCommon'),
  serialized_pb=_b('\n\x19proto/common/tariff.proto\x12\x0cproto.common\x1a\x18proto/common/types.proto\"\xb7\x01\n\x06Tariff\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12*\n\x06status\x18\x03 \x01(\x0e\x32\x1a.proto.common.TariffStatus\x12\x31\n\ttrade_tax\x18\x04 \x01(\x0b\x32\x1a.proto.common.DecimalValueB\x02\x18\x01\x12\r\n\x05\x64\x65scr\x18\x05 \x01(\t\x12\"\n\x03tax\x18\x06 \x01(\x0b\x32\x15.proto.common.Decimal*z\n\x0cTariffStatus\x12\x19\n\x15TARIFF_STATUS_UNKNOWN\x10\x00\x12\x18\n\x14TARIFF_STATUS_ACTIVE\x10\x01\x12\x19\n\x15TARIFF_STATUS_PENDING\x10\x02\x12\x1a\n\x16TARIFF_STATUS_INACTIVE\x10\x03\x42\x10P\x01\xa2\x02\x0bProtoCommonb\x06proto3')
  ,
  dependencies=[proto_dot_common_dot_types__pb2.DESCRIPTOR,])

_TARIFFSTATUS = _descriptor.EnumDescriptor(
  name='TariffStatus',
  full_name='proto.common.TariffStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TARIFF_STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARIFF_STATUS_ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARIFF_STATUS_PENDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARIFF_STATUS_INACTIVE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=255,
  serialized_end=377,
)
_sym_db.RegisterEnumDescriptor(_TARIFFSTATUS)

TariffStatus = enum_type_wrapper.EnumTypeWrapper(_TARIFFSTATUS)
TARIFF_STATUS_UNKNOWN = 0
TARIFF_STATUS_ACTIVE = 1
TARIFF_STATUS_PENDING = 2
TARIFF_STATUS_INACTIVE = 3



_TARIFF = _descriptor.Descriptor(
  name='Tariff',
  full_name='proto.common.Tariff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='proto.common.Tariff.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='proto.common.Tariff.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.common.Tariff.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_tax', full_name='proto.common.Tariff.trade_tax', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descr', full_name='proto.common.Tariff.descr', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tax', full_name='proto.common.Tariff.tax', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=70,
  serialized_end=253,
)

_TARIFF.fields_by_name['status'].enum_type = _TARIFFSTATUS
_TARIFF.fields_by_name['trade_tax'].message_type = proto_dot_common_dot_types__pb2._DECIMALVALUE
_TARIFF.fields_by_name['tax'].message_type = proto_dot_common_dot_types__pb2._DECIMAL
DESCRIPTOR.message_types_by_name['Tariff'] = _TARIFF
DESCRIPTOR.enum_types_by_name['TariffStatus'] = _TARIFFSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tariff = _reflection.GeneratedProtocolMessageType('Tariff', (_message.Message,), {
  'DESCRIPTOR' : _TARIFF,
  '__module__' : 'proto.common.tariff_pb2'
  # @@protoc_insertion_point(class_scope:proto.common.Tariff)
  })
_sym_db.RegisterMessage(Tariff)


DESCRIPTOR._options = None
_TARIFF.fields_by_name['trade_tax']._options = None
# @@protoc_insertion_point(module_scope)