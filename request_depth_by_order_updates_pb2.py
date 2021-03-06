# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_depth_by_order_updates.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_depth_by_order_updates.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$request_depth_by_order_updates.proto\x12\x03rti\"\xeb\x01\n\x1aRequestDepthByOrderUpdates\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12:\n\x07request\x18\xa0\x8d\x06 \x01(\x0e\x32\'.rti.RequestDepthByOrderUpdates.Request\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x15\n\x0b\x64\x65pth_price\x18\xa5\xb6\t \x01(\x01\")\n\x07Request\x12\r\n\tSUBSCRIBE\x10\x01\x12\x0f\n\x0bUNSUBSCRIBE\x10\x02')
)



_REQUESTDEPTHBYORDERUPDATES_REQUEST = _descriptor.EnumDescriptor(
  name='Request',
  full_name='rti.RequestDepthByOrderUpdates.Request',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUBSCRIBE', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=240,
  serialized_end=281,
)
_sym_db.RegisterEnumDescriptor(_REQUESTDEPTHBYORDERUPDATES_REQUEST)


_REQUESTDEPTHBYORDERUPDATES = _descriptor.Descriptor(
  name='RequestDepthByOrderUpdates',
  full_name='rti.RequestDepthByOrderUpdates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.RequestDepthByOrderUpdates.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.RequestDepthByOrderUpdates.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='rti.RequestDepthByOrderUpdates.request', index=2,
      number=100000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.RequestDepthByOrderUpdates.symbol', index=3,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.RequestDepthByOrderUpdates.exchange', index=4,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth_price', full_name='rti.RequestDepthByOrderUpdates.depth_price', index=5,
      number=154405, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTDEPTHBYORDERUPDATES_REQUEST,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=281,
)

_REQUESTDEPTHBYORDERUPDATES.fields_by_name['request'].enum_type = _REQUESTDEPTHBYORDERUPDATES_REQUEST
_REQUESTDEPTHBYORDERUPDATES_REQUEST.containing_type = _REQUESTDEPTHBYORDERUPDATES
DESCRIPTOR.message_types_by_name['RequestDepthByOrderUpdates'] = _REQUESTDEPTHBYORDERUPDATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestDepthByOrderUpdates = _reflection.GeneratedProtocolMessageType('RequestDepthByOrderUpdates', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDEPTHBYORDERUPDATES,
  __module__ = 'request_depth_by_order_updates_pb2'
  # @@protoc_insertion_point(class_scope:rti.RequestDepthByOrderUpdates)
  ))
_sym_db.RegisterMessage(RequestDepthByOrderUpdates)


# @@protoc_insertion_point(module_scope)
