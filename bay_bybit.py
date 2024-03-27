from pybit.unified_trading import HTTP
from pprint import pprint
session = HTTP(
    testnet=True,
    api_key="NtB4xBIus7a7L4jeWh",
    api_secret="DljgYuJdmnPPutCJmk35sZguXeTm6UNR2YxH",
) 

pprint(session.place_order(
    category="spot",
    symbol="SOLUSDT",
    side="Sell",
    orderType="Market",
    qty="0.35",
    timeInForce="GTC",
    # orderLinkId="spot",
    isLeverage=0,
    orderFilter="Order",
   
))


