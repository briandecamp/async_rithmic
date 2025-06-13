import enum

from . import protocol_buffers as pb

class DataType(enum.Enum):
    LAST_TRADE = 1
    BBO = 2
    ORDER_BOOK = 4
    OPEN = 8
    OPENING_INDICATOR = 16
    HIGH_LOW = 32
    HIGH_BID_LOW_ASK = 64
    CLOSE = 128
    CLOSING_INDICATOR = 256
    SETTLEMENT = 512
    MARKET_MODE = 1024
    OPEN_INTEREST = 2048
    MARGIN_RATE = 4096
    HIGH_PRICE_LIMIT = 8192
    LOW_PRICE_LIMIT = 16384
    PROJECTED_SETTLEMENT = 32768

OrderType = pb.request_new_order_pb2.RequestNewOrder.PriceType
OrderDuration = pb.request_new_order_pb2.RequestNewOrder.Duration
TransactionType = pb.request_new_order_pb2.RequestNewOrder.TransactionType

LastTradePresenceBits = pb.last_trade_pb2.LastTrade.PresenceBits
ExchangeOrderNotificationType = pb.exchange_order_notification_pb2.ExchangeOrderNotification.NotifyType

TimeBarType = pb.request_time_bar_replay_pb2.RequestTimeBarReplay.BarType

InstrumentType = pb.request_search_symbols_pb2.RequestSearchSymbols.InstrumentType
SearchPattern = pb.request_search_symbols_pb2.RequestSearchSymbols.Pattern

class Gateway(enum.Enum):
    TEST = "rituz00100.rithmic.com:443"

    CHICAGO = "rprotocol.rithmic.com:443"
    SYDNEY = "au.rithmic.com:443"
    SAO_PAULO = "br.rithmic.com:443"
    COLO75 = "colo75.rithmic.com:443"
    FRANKFURT = "de.rithmic.com:443"
    HONGKONG = "hk.rithmic.com:443"
    IRELAND = "ie.rithmic.com:443"
    MUMBAI = "in.rithmic.com:443"
    SEOUL = "kr.rithmic.com:443"
    CAPETOWN = "za.rithmic.com:443"
    TOKYO = "jp.rithmic.com:443"
    SINGAPORE = "sg.rithmic.com:443"
