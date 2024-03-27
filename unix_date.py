#api_key = 'VTes1twYO08Ps9zJRz'
#api_secret = '1wMh5bh4FyuQGxOAz9eSazgXDQbKwNvSCgKF'
import time
from pybit.unified_trading import HTTP
session = HTTP(testnet=True)
import pandas as pd
from datetime import datetime
from pprint import pprint as pp
unix_time = (int(time.time())*1000)
end_s = (unix_time - 88694000) # минус 1 сутки
# Выполнение запроса для получения свечей
from pybit.unified_trading import HTTP
while end_s < unix_time:  
	
	session = HTTP(testnet=True)
	response = session.get_kline(
		category="inverse",
		symbol="ETHUSD",
		interval=1,
		start=end_s,
		end=unix_time,
		)
	end_s += 100000000
	
# Преобразование данных в формат DataFrame библиотеки Pandas
	my_list = response['result']['list']
	#first_numbers = [("Timestamp('" + datetime.utcfromtimestamp(int(sublist[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S') + "')", sublist[1], sublist[2], sublist[3], sublist[4], sublist[5]) for sublist in my_list]
	dfd = [{'open': float(sublist[1]), 'close': float(sublist[2]), 'high': float(sublist[3]), 'low': float(sublist[4]), 'value': float(sublist[6]), 'volume': int(sublist[5]), 'begin': datetime.utcfromtimestamp((int(sublist[0])-60) / 1000).strftime('%Y-%m-%d %H:%M:%S'), 'end': datetime.utcfromtimestamp((int(sublist[0])-1) / 1000).strftime('%Y-%m-%d %H:%M:59')} for sublist in my_list]
	first_numbers = sorted(dfd, key=lambda x: x['end'])
	#pp(first_numbers[0])

	
	#first_numbers = [(sublist[1], sublist[2], sublist[3], sublist[4], sublist[5], datetime.utcfromtimestamp(int(sublist[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S')) for sublist in my_list]
	
	# [{'open': 295.77, 'close': 295.77, 'high': 295.77, 'low': 295.77, 'value': 4655419.800000005, 'volume': 15740, 'begin': '2024-03-22 09:59:00', 'end': '2024-03-22 09:59:59'}]
	#print(first_numbers)


	
	#df = pd.DataFrame(first_numbers)
	#df.columns = ["datetime", "open", "high", "low", "close", "volume"]
	#dfd = df.reindex(index=df.index[::-1])
	#dfd.to_csv('data.csv', mode='a', header=False, index=False)
	#print(df)
	
#df.to_csv('data.csv', index=False)

