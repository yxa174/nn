# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/tradeapi/v1/stops.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from FinamPy.proto.tradeapi.v1 import common_pb2 as proto_dot_tradeapi_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dproto/tradeapi/v1/stops.proto\x12\x11proto.tradeapi.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1eproto/tradeapi/v1/common.proto\"\xab\x05\n\x04Stop\x12\x0f\n\x07stop_id\x18\x01 \x01(\x05\x12\x15\n\rsecurity_code\x18\x02 \x01(\t\x12\x16\n\x0esecurity_board\x18\x03 \x01(\t\x12)\n\x06market\x18\x04 \x01(\x0e\x32\x19.proto.tradeapi.v1.Market\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12,\n\x08\x62uy_sell\x18\x06 \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12\x33\n\x0f\x65xpiration_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nlink_order\x18\x08 \x01(\x03\x12\x39\n\x0cvalid_before\x18\t \x01(\x0b\x32#.proto.tradeapi.v1.OrderValidBefore\x12-\n\x06status\x18\n \x01(\x0e\x32\x1d.proto.tradeapi.v1.StopStatus\x12\x0f\n\x07message\x18\x0b \x01(\t\x12\x10\n\x08order_no\x18\x0c \x01(\x03\x12\x10\n\x08trade_no\x18\r \x01(\x03\x12/\n\x0b\x61\x63\x63\x65pted_at\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63\x61nceled_at\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x63urrency\x18\x10 \x01(\t\x12\x1c\n\x14take_profit_extremum\x18\x11 \x01(\x01\x12\x19\n\x11take_profit_level\x18\x12 \x01(\x01\x12.\n\tstop_loss\x18\x13 \x01(\x0b\x32\x1b.proto.tradeapi.v1.StopLoss\x12\x32\n\x0btake_profit\x18\x14 \x01(\x0b\x32\x1d.proto.tradeapi.v1.TakeProfit\"\x9e\x01\n\x08StopLoss\x12\x18\n\x10\x61\x63tivation_price\x18\x01 \x01(\x01\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x14\n\x0cmarket_price\x18\x03 \x01(\x08\x12\x31\n\x08quantity\x18\x04 \x01(\x0b\x32\x1f.proto.tradeapi.v1.StopQuantity\x12\x0c\n\x04time\x18\x05 \x01(\x05\x12\x12\n\nuse_credit\x18\x06 \x01(\x08\"\xfd\x01\n\nTakeProfit\x12\x18\n\x10\x61\x63tivation_price\x18\x01 \x01(\x01\x12\x36\n\x10\x63orrection_price\x18\x02 \x01(\x0b\x32\x1c.proto.tradeapi.v1.StopPrice\x12\x32\n\x0cspread_price\x18\x03 \x01(\x0b\x32\x1c.proto.tradeapi.v1.StopPrice\x12\x14\n\x0cmarket_price\x18\x04 \x01(\x08\x12\x31\n\x08quantity\x18\x05 \x01(\x0b\x32\x1f.proto.tradeapi.v1.StopQuantity\x12\x0c\n\x04time\x18\x06 \x01(\x05\x12\x12\n\nuse_credit\x18\x07 \x01(\x08\"R\n\x0cStopQuantity\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x33\n\x05units\x18\x02 \x01(\x0e\x32$.proto.tradeapi.v1.StopQuantityUnits\"L\n\tStopPrice\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x30\n\x05units\x18\x02 \x01(\x0e\x32!.proto.tradeapi.v1.StopPriceUnits\"7\n\x11\x43\x61ncelStopRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0f\n\x07stop_id\x18\x02 \x01(\x05\"6\n\x10\x43\x61ncelStopResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0f\n\x07stop_id\x18\x02 \x01(\x05\"p\n\x0fGetStopsRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x18\n\x10include_executed\x18\x02 \x01(\x08\x12\x18\n\x10include_canceled\x18\x03 \x01(\x08\x12\x16\n\x0einclude_active\x18\x04 \x01(\x08\"K\n\x0eGetStopsResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12&\n\x05stops\x18\x02 \x03(\x0b\x32\x17.proto.tradeapi.v1.Stop\"\xe8\x02\n\x0eNewStopRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0esecurity_board\x18\x02 \x01(\t\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\x12,\n\x08\x62uy_sell\x18\x04 \x01(\x0e\x32\x1a.proto.tradeapi.v1.BuySell\x12.\n\tstop_loss\x18\x05 \x01(\x0b\x32\x1b.proto.tradeapi.v1.StopLoss\x12\x32\n\x0btake_profit\x18\x06 \x01(\x0b\x32\x1d.proto.tradeapi.v1.TakeProfit\x12\x33\n\x0f\x65xpiration_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nlink_order\x18\x08 \x01(\x03\x12\x39\n\x0cvalid_before\x18\t \x01(\x0b\x32#.proto.tradeapi.v1.OrderValidBefore\"b\n\rNewStopResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0f\n\x07stop_id\x18\x02 \x01(\x05\x12\x15\n\rsecurity_code\x18\x03 \x01(\t\x12\x16\n\x0esecurity_board\x18\x04 \x01(\t*\x8c\x01\n\nStopStatus\x12\x1b\n\x17STOP_STATUS_UNSPECIFIED\x10\x00\x12\x14\n\x10STOP_STATUS_NONE\x10\x01\x12\x16\n\x12STOP_STATUS_ACTIVE\x10\x02\x12\x19\n\x15STOP_STATUS_CANCELLED\x10\x03\x12\x18\n\x14STOP_STATUS_EXECUTED\x10\x04*w\n\x11StopQuantityUnits\x12#\n\x1fSTOP_QUANTITY_UNITS_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSTOP_QUANTITY_UNITS_PERCENT\x10\x01\x12\x1c\n\x18STOP_QUANTITY_UNITS_LOTS\x10\x02*k\n\x0eStopPriceUnits\x12 \n\x1cSTOP_PRICE_UNITS_UNSPECIFIED\x10\x00\x12\x1c\n\x18STOP_PRICE_UNITS_PERCENT\x10\x01\x12\x19\n\x15STOP_PRICE_UNITS_PIPS\x10\x02\x42\x1a\xaa\x02\x17\x46inam.TradeApi.Proto.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.tradeapi.v1.stops_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\027Finam.TradeApi.Proto.V1'
  _globals['_STOPSTATUS']._serialized_start=2150
  _globals['_STOPSTATUS']._serialized_end=2290
  _globals['_STOPQUANTITYUNITS']._serialized_start=2292
  _globals['_STOPQUANTITYUNITS']._serialized_end=2411
  _globals['_STOPPRICEUNITS']._serialized_start=2413
  _globals['_STOPPRICEUNITS']._serialized_end=2520
  _globals['_STOP']._serialized_start=118
  _globals['_STOP']._serialized_end=801
  _globals['_STOPLOSS']._serialized_start=804
  _globals['_STOPLOSS']._serialized_end=962
  _globals['_TAKEPROFIT']._serialized_start=965
  _globals['_TAKEPROFIT']._serialized_end=1218
  _globals['_STOPQUANTITY']._serialized_start=1220
  _globals['_STOPQUANTITY']._serialized_end=1302
  _globals['_STOPPRICE']._serialized_start=1304
  _globals['_STOPPRICE']._serialized_end=1380
  _globals['_CANCELSTOPREQUEST']._serialized_start=1382
  _globals['_CANCELSTOPREQUEST']._serialized_end=1437
  _globals['_CANCELSTOPRESULT']._serialized_start=1439
  _globals['_CANCELSTOPRESULT']._serialized_end=1493
  _globals['_GETSTOPSREQUEST']._serialized_start=1495
  _globals['_GETSTOPSREQUEST']._serialized_end=1607
  _globals['_GETSTOPSRESULT']._serialized_start=1609
  _globals['_GETSTOPSRESULT']._serialized_end=1684
  _globals['_NEWSTOPREQUEST']._serialized_start=1687
  _globals['_NEWSTOPREQUEST']._serialized_end=2047
  _globals['_NEWSTOPRESULT']._serialized_start=2049
  _globals['_NEWSTOPRESULT']._serialized_end=2147
# @@protoc_insertion_point(module_scope)
