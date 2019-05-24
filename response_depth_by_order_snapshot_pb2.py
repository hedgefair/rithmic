# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_depth_by_order_snapshot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_depth_by_order_snapshot.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&response_depth_by_order_snapshot.proto\x12\x03rti\"\x94\x03\n\x1cResponseDepthByOrderSnapshot\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x1c\n\x12rq_handler_rp_code\x18\x9c\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x19\n\x0fsequence_number\x18\x82\xeb\x06 \x01(\x04\x12G\n\ndepth_side\x18\x8c\xb0\t \x01(\x0e\x32\x31.rti.ResponseDepthByOrderSnapshot.TransactionType\x12\x15\n\x0b\x64\x65pth_price\x18\xa5\xb6\t \x01(\x01\x12\x14\n\ndepth_size\x18\xa6\xb6\t \x03(\x05\x12\x1e\n\x14\x64\x65pth_order_priority\x18\x8d\xb0\t \x03(\x04\x12\x1b\n\x11\x65xchange_order_id\x18\xf6\x8d\t \x03(\t\"$\n\x0fTransactionType\x12\x07\n\x03\x42UY\x10\x01\x12\x08\n\x04SELL\x10\x02')
)



_RESPONSEDEPTHBYORDERSNAPSHOT_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='rti.ResponseDepthByOrderSnapshot.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELL', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=416,
  serialized_end=452,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEDEPTHBYORDERSNAPSHOT_TRANSACTIONTYPE)


_RESPONSEDEPTHBYORDERSNAPSHOT = _descriptor.Descriptor(
  name='ResponseDepthByOrderSnapshot',
  full_name='rti.ResponseDepthByOrderSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseDepthByOrderSnapshot.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseDepthByOrderSnapshot.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rq_handler_rp_code', full_name='rti.ResponseDepthByOrderSnapshot.rq_handler_rp_code', index=2,
      number=132764, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseDepthByOrderSnapshot.rp_code', index=3,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.ResponseDepthByOrderSnapshot.exchange', index=4,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.ResponseDepthByOrderSnapshot.symbol', index=5,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='rti.ResponseDepthByOrderSnapshot.sequence_number', index=6,
      number=112002, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_side', full_name='rti.ResponseDepthByOrderSnapshot.depth_side', index=7,
      number=153612, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_price', full_name='rti.ResponseDepthByOrderSnapshot.depth_price', index=8,
      number=154405, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_size', full_name='rti.ResponseDepthByOrderSnapshot.depth_size', index=9,
      number=154406, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_order_priority', full_name='rti.ResponseDepthByOrderSnapshot.depth_order_priority', index=10,
      number=153613, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_order_id', full_name='rti.ResponseDepthByOrderSnapshot.exchange_order_id', index=11,
      number=149238, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEDEPTHBYORDERSNAPSHOT_TRANSACTIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=452,
)

_RESPONSEDEPTHBYORDERSNAPSHOT.fields_by_name['depth_side'].enum_type = _RESPONSEDEPTHBYORDERSNAPSHOT_TRANSACTIONTYPE
_RESPONSEDEPTHBYORDERSNAPSHOT_TRANSACTIONTYPE.containing_type = _RESPONSEDEPTHBYORDERSNAPSHOT
DESCRIPTOR.message_types_by_name['ResponseDepthByOrderSnapshot'] = _RESPONSEDEPTHBYORDERSNAPSHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseDepthByOrderSnapshot = _reflection.GeneratedProtocolMessageType('ResponseDepthByOrderSnapshot', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEDEPTHBYORDERSNAPSHOT,
  __module__ = 'response_depth_by_order_snapshot_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseDepthByOrderSnapshot)
  ))
_sym_db.RegisterMessage(ResponseDepthByOrderSnapshot)


# @@protoc_insertion_point(module_scope)