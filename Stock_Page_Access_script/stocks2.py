import requests
import webbrowser
import investpy


if __name__ == "__main__":
	while True:
		print(">>",end = "")
		el = input() 
		if el == "exit":
			break

		try:	
			flag = True
			search_result = investpy.search_quotes(text=el, products=['stocks'],countries=['india'])
			
			for i in search_result:
				if i.exchange == 'NSE':
					stock_link = i.tag
					stock_name = i.name
					flag = False
					break
			if flag:
				raise Exception('Keyword not specific.')

			header={'User-agent': 'Mozilla/5.0'}
			quote_url = "https://tvdb.brianthe.dev/search?q="+el+"&sc=india"
			quote_page=requests.get(quote_url,headers=header)
			quote_json = quote_page.json()

			for i in quote_json['r']:
    				if i[1] == 'NSE':
       					quote = i[2]
        				break

			rs_url = "https://in.investing.com"+stock_link+"-technical"
			rs_url2 = "https://in.tradingview.com/chart/H6JzImxu/?symbol=NSE%3A"+quote
		
			webbrowser.open(rs_url2)
			webbrowser.open_new_tab(rs_url)
			print(stock_name)
		except:
 			print("Keyword not specific.")
	