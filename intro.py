import pandas as pd
import quandl
import requests

from confidential import api_key

def get_data():

	# quandl.ApiConfig.api_key = 'ePrqYQi-GtKkA5mzxLDA'

	# data = quandl.get_table("WIKI/PRICES", paginate=True)
	# print(data)

	quandl.ApiConfig.api_key = api_key

	# data = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES?date=1999-11-18&ticker=A&api_key=ePrqYQi-GtKkA5mzxLDA')
	# print(data.json())

	data = quandl.get("WIKI/GOOGL")
	print(data.tail())
	# df = Quandl.get(' ')

	# df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

def main():
	get_data()

if __name__ == '__main__':
	main()

