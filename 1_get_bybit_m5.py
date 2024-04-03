#api_key = 'VTes1twYO08Ps9zJRz'
#api_secret = '1wMh5bh4FyuQGxOAz9eSazgXDQbKwNvSCgKF'
from pybit.unified_trading import HTTP
session = HTTP(testnet=True)
import my_config.trade_config
import pandas as pd
from datetime import datetime
import os
end_s = 1611022694000
coin = my_config.trade_config.Config.training_NN.pop()
file_path = 'csv/{}_H1.csv'.format(coin)
if os.path.exists(file_path):
    os.remove(file_path)
else:
	pass
with open(file_path, 'w') as file:
    file.write('datetime,open,high,low,close,volume\n')
while end_s < 1710926293000:
	
	session = HTTP(testnet=True)
	response = session.get_kline(
		category="inverse",
		symbol="{}".format(coin),
		interval=60,
		start=1610922694000,
		end=end_s,
		)
	end_s += 100000000
# Преобразование данных в формат DataFrame библиотеки Pandas

	my_list = response['result']['list']

	first_numbers = [(datetime.utcfromtimestamp(int(sublist[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S'),float(sublist[1]), float(sublist[2]), float(sublist[3]), float(sublist[4]), round(float(sublist[5]))) for sublist in my_list]
	df = pd.DataFrame(first_numbers)
	dfd = df.reindex(index=df.index[::-1])
	dfd.to_csv(file_path, mode='a', header=False, index=False)
	print(df)
	
#df.to_csv('data.csv', index=False)
