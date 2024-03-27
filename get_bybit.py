#api_key = 'VTes1twYO08Ps9zJRz'
#api_secret = '1wMh5bh4FyuQGxOAz9eSazgXDQbKwNvSCgKF'
from pybit.unified_trading import HTTP
session = HTTP(testnet=True)
import pandas as pd
from datetime import datetime
#
# Выполнение запроса для получения свечей
from pybit.unified_trading import HTTP
end_s = 1611022694000
while end_s < 1710926293000:
	
	session = HTTP(testnet=True)
	response = session.get_kline(
		category="inverse",
		symbol="BTCUSD",
		interval=15,
		start=1610922694000,
		end=end_s,
		)
	end_s += 100000000
# Преобразование данных в формат DataFrame библиотеки Pandas

	my_list = response['result']['list']

	first_numbers = [(datetime.utcfromtimestamp(int(sublist[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S'),sublist[1], sublist[2], sublist[3], sublist[5], sublist[6]) for sublist in my_list]
	df = pd.DataFrame(first_numbers)
	#df.columns = ["datetime", "open", "high", "low", "close", "volume"]
	dfd = df.reindex(index=df.index[::-1])
	dfd.to_csv('data.csv', mode='a', header=False, index=False)
	print(df)
	
#df.to_csv('data.csv', index=False)
