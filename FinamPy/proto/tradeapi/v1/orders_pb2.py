# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/tradeapi/v1/orders.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from FinamPy.proto.tradeapi.v1 import common_pb2 as proto_dot_tradeapi_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eproto/tradeapi/v1/orders.proto\x12\x11proto.tradeapi.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1eproto/tradeapi/v1/common.proto\"~\n\x0eOrderCondition\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32%.proto.tradeapi.v1.OrderConditionType\x12\r\n\x05price\x18\x02 \x01(\x01\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf9\x02\n\x0fNewOrderRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0esecurity_board\x18\x02 \x01(\t\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\x12,\n\x08\x62uy_sell\x18\x04 \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12\x10\n\x08quantity\x18\x05 \x01(\x05\x12\x12\n\nuse_credit\x18\x06 \x01(\x08\x12+\n\x05price\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x32\n\x08property\x18\x08 \x01(\x0e\x32 .proto.tradeapi.v1.OrderProperty\x12\x34\n\tcondition\x18\t \x01(\x0b\x32!.proto.tradeapi.v1.OrderCondition\x12\x39\n\x0cvalid_before\x18\n \x01(\x0b\x32#.proto.tradeapi.v1.OrderValidBefore\"R\n\x0eNewOrderResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x05\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\"?\n\x12\x43\x61ncelOrderRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x05\">\n\x11\x43\x61ncelOrderResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x05\"p\n\x10GetOrdersRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x17\n\x0finclude_matched\x18\x02 \x01(\x08\x12\x18\n\x10include_canceled\x18\x03 \x01(\x08\x12\x16\n\x0einclude_active\x18\x04 \x01(\x08\"\xa3\x04\n\x05Order\x12\x10\n\x08order_no\x18\x01 \x01(\x03\x12\x16\n\x0etransaction_id\x18\x02 \x01(\x05\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12.\n\x06status\x18\x05 \x01(\x0e\x32\x1e.proto.tradeapi.v1.OrderStatus\x12,\n\x08\x62uy_sell\x18\x06 \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05price\x18\x08 \x01(\x01\x12\x10\n\x08quantity\x18\t \x01(\x05\x12\x0f\n\x07\x62\x61lance\x18\n \x01(\x05\x12\x0f\n\x07message\x18\x0b \x01(\t\x12\x10\n\x08\x63urrency\x18\x0c \x01(\t\x12\x34\n\tcondition\x18\r \x01(\x0b\x32!.proto.tradeapi.v1.OrderCondition\x12\x39\n\x0cvalid_before\x18\x0e \x01(\x0b\x32#.proto.tradeapi.v1.OrderValidBefore\x12/\n\x0b\x61\x63\x63\x65pted_at\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0esecurity_board\x18\x10 \x01(\t\x12)\n\x06market\x18\x11 \x01(\x0e\x32\x19.proto.tradeapi.v1.Market\"N\n\x0fGetOrdersResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12(\n\x06orders\x18\x02 \x03(\x0b\x32\x18.proto.tradeapi.v1.Order*\x95\x01\n\rOrderProperty\x12\x1e\n\x1aORDER_PROPERTY_UNSPECIFIED\x10\x00\x12\x1f\n\x1bORDER_PROPERTY_PUT_IN_QUEUE\x10\x01\x12!\n\x1dORDER_PROPERTY_CANCEL_BALANCE\x10\x02\x12 \n\x1cORDER_PROPERTY_IMM_OR_CANCEL\x10\x03*\xeb\x02\n\x12OrderConditionType\x12$\n ORDER_CONDITION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18ORDER_CONDITION_TYPE_BID\x10\x01\x12$\n ORDER_CONDITION_TYPE_BID_OR_LAST\x10\x02\x12\x1c\n\x18ORDER_CONDITION_TYPE_ASK\x10\x03\x12$\n ORDER_CONDITION_TYPE_ASK_OR_LAST\x10\x04\x12\x1d\n\x19ORDER_CONDITION_TYPE_TIME\x10\x05\x12!\n\x1dORDER_CONDITION_TYPE_COV_DOWN\x10\x06\x12\x1f\n\x1bORDER_CONDITION_TYPE_COV_UP\x10\x07\x12 \n\x1cORDER_CONDITION_TYPE_LAST_UP\x10\x08\x12\"\n\x1eORDER_CONDITION_TYPE_LAST_DOWN\x10\t*\x91\x01\n\x0bOrderStatus\x12\x1c\n\x18ORDER_STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11ORDER_STATUS_NONE\x10\x01\x12\x17\n\x13ORDER_STATUS_ACTIVE\x10\x02\x12\x1a\n\x16ORDER_STATUS_CANCELLED\x10\x03\x12\x18\n\x14ORDER_STATUS_MATCHED\x10\x04\x42\x1a\xaa\x02\x17\x46inam.TradeApi.Proto.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.tradeapi.v1.orders_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\027Finam.TradeApi.Proto.V1'
  _globals['_ORDERPROPERTY']._serialized_start=1616
  _globals['_ORDERPROPERTY']._serialized_end=1765
  _globals['_ORDERCONDITIONTYPE']._serialized_start=1768
  _globals['_ORDERCONDITIONTYPE']._serialized_end=2131
  _globals['_ORDERSTATUS']._serialized_start=2134
  _globals['_ORDERSTATUS']._serialized_end=2279
  _globals['_ORDERCONDITION']._serialized_start=150
  _globals['_ORDERCONDITION']._serialized_end=276
  _globals['_NEWORDERREQUEST']._serialized_start=279
  _globals['_NEWORDERREQUEST']._serialized_end=656
  _globals['_NEWORDERRESULT']._serialized_start=658
  _globals['_NEWORDERRESULT']._serialized_end=740
  _globals['_CANCELORDERREQUEST']._serialized_start=742
  _globals['_CANCELORDERREQUEST']._serialized_end=805
  _globals['_CANCELORDERRESULT']._serialized_start=807
  _globals['_CANCELORDERRESULT']._serialized_end=869
  _globals['_GETORDERSREQUEST']._serialized_start=871
  _globals['_GETORDERSREQUEST']._serialized_end=983
  _globals['_ORDER']._serialized_start=986
  _globals['_ORDER']._serialized_end=1533
  _globals['_GETORDERSRESULT']._serialized_start=1535
  _globals['_GETORDERSRESULT']._serialized_end=1613
# @@protoc_insertion_point(module_scope)
