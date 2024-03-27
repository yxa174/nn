#key NtB4xBIus7a7L4jeWh
#secret DljgYuJdmnPPutCJmk35sZguXeTm6UNR2YxH
from pprint import pprint
from pybit.unified_trading import HTTP
session = HTTP(
    testnet=True,
    api_key="NtB4xBIus7a7L4jeWh",
    api_secret="DljgYuJdmnPPutCJmk35sZguXeTm6UNR2YxH",
)
data = session.get_wallet_balance(
    accountType="SPOT",
   
) 
n = (len(data['result']['list'][0]['coin']))
print('Всего монет:', n)
free_balance = data['result']['list'][0]['coin'][0]['free']
for i in range(n):
    print(data['result']['list'][0]['coin'][i]['coin'], data['result']['list'][0]['coin'][i]['walletBalance'])
