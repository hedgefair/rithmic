# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indicator_prices.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='indicator_prices.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x16indicator_prices.proto\x12\x03rti\"\xae\x02\n\x0fIndicatorPrices\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x14\n\nclear_bits\x18\xcb\xb7\t \x01(\r\x12\x15\n\x0bis_snapshot\x18\xa9\xdc\x06 \x01(\x08\x12\x1b\n\x11opening_indicator\x18\x9a\xb7\t \x01(\x01\x12\x1b\n\x11\x63losing_indicator\x18\xd0\xb3\t \x01(\x01\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05\"<\n\x0cPresenceBits\x12\x15\n\x11OPENING_INDICATOR\x10\x01\x12\x15\n\x11\x43LOSING_INDICATOR\x10\x02')
)



_INDICATORPRICES_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.IndicatorPrices.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPENING_INDICATOR', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSING_INDICATOR', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=274,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_INDICATORPRICES_PRESENCEBITS)


_INDICATORPRICES = _descriptor.Descriptor(
  name='IndicatorPrices',
  full_name='rti.IndicatorPrices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.IndicatorPrices.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.IndicatorPrices.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.IndicatorPrices.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.IndicatorPrices.presence_bits', index=3,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_bits', full_name='rti.IndicatorPrices.clear_bits', index=4,
      number=154571, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_snapshot', full_name='rti.IndicatorPrices.is_snapshot', index=5,
      number=110121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opening_indicator', full_name='rti.IndicatorPrices.opening_indicator', index=6,
      number=154522, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closing_indicator', full_name='rti.IndicatorPrices.closing_indicator', index=7,
      number=154064, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.IndicatorPrices.ssboe', index=8,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.IndicatorPrices.usecs', index=9,
      number=150101, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INDICATORPRICES_PRESENCEBITS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=334,
)

_INDICATORPRICES_PRESENCEBITS.containing_type = _INDICATORPRICES
DESCRIPTOR.message_types_by_name['IndicatorPrices'] = _INDICATORPRICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndicatorPrices = _reflection.GeneratedProtocolMessageType('IndicatorPrices', (_message.Message,), dict(
  DESCRIPTOR = _INDICATORPRICES,
  __module__ = 'indicator_prices_pb2'
  # @@protoc_insertion_point(class_scope:rti.IndicatorPrices)
  ))
_sym_db.RegisterMessage(IndicatorPrices)


# @@protoc_insertion_point(module_scope)