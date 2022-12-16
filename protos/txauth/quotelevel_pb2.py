# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/common/quotelevel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/common/quotelevel.proto',
  package='proto.common',
  syntax='proto3',
  serialized_options=_b('B\024QuoteLevelOuterClassP\001\242\002\013ProtoCommon'),
  serialized_pb=_b('\n\x1dproto/common/quotelevel.proto\x12\x0cproto.common*n\n\nQuoteLevel\x12\x0e\n\nLAST_PRICE\x10\x00\x12\x12\n\x0e\x42\x45ST_BID_OFFER\x10\x01\x12\x13\n\x0f\x44\x45PTH_OF_MARKET\x10\x02\x12\x11\n\rDEPTH_OF_BOOK\x10\x03\x12\x14\n\x10\x41\x43\x43\x45SS_FORBIDDEN\x10\x04\x42&B\x14QuoteLevelOuterClassP\x01\xa2\x02\x0bProtoCommonb\x06proto3')
)

_QUOTELEVEL = _descriptor.EnumDescriptor(
  name='QuoteLevel',
  full_name='proto.common.QuoteLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LAST_PRICE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEST_BID_OFFER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPTH_OF_MARKET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPTH_OF_BOOK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_FORBIDDEN', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=47,
  serialized_end=157,
)
_sym_db.RegisterEnumDescriptor(_QUOTELEVEL)

QuoteLevel = enum_type_wrapper.EnumTypeWrapper(_QUOTELEVEL)
LAST_PRICE = 0
BEST_BID_OFFER = 1
DEPTH_OF_MARKET = 2
DEPTH_OF_BOOK = 3
ACCESS_FORBIDDEN = 4


DESCRIPTOR.enum_types_by_name['QuoteLevel'] = _QUOTELEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
