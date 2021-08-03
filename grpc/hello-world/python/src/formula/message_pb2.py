# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_options=b'\n\030io.grpc.examples.messageB\014MessageProtoP\001\242\002\003MSG',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x07message\"=\n\x0eMessageRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\"\x1f\n\x0cMessageReply\x12\x0f\n\x07message\x18\x01 \x01(\t2F\n\x07Message\x12;\n\x07Message\x12\x17.message.MessageRequest\x1a\x15.message.MessageReply\"\x00\x42\x30\n\x18io.grpc.examples.messageB\x0cMessageProtoP\x01\xa2\x02\x03MSGb\x06proto3'
)




_MESSAGEREQUEST = _descriptor.Descriptor(
  name='MessageRequest',
  full_name='message.MessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='message.MessageRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='message.MessageRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='surname', full_name='message.MessageRequest.surname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=26,
  serialized_end=87,
)


_MESSAGEREPLY = _descriptor.Descriptor(
  name='MessageReply',
  full_name='message.MessageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='message.MessageReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=89,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['MessageRequest'] = _MESSAGEREQUEST
DESCRIPTOR.message_types_by_name['MessageReply'] = _MESSAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageRequest = _reflection.GeneratedProtocolMessageType('MessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.MessageRequest)
  })
_sym_db.RegisterMessage(MessageRequest)

MessageReply = _reflection.GeneratedProtocolMessageType('MessageReply', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEREPLY,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.MessageReply)
  })
_sym_db.RegisterMessage(MessageReply)


DESCRIPTOR._options = None

_MESSAGE = _descriptor.ServiceDescriptor(
  name='Message',
  full_name='message.Message',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=192,
  methods=[
  _descriptor.MethodDescriptor(
    name='Message',
    full_name='message.Message.Message',
    index=0,
    containing_service=None,
    input_type=_MESSAGEREQUEST,
    output_type=_MESSAGEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSAGE)

DESCRIPTOR.services_by_name['Message'] = _MESSAGE

# @@protoc_insertion_point(module_scope)