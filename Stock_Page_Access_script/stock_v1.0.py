from bs4 import BeautifulSoup
import requests
import sys
import webbrowser
import json

if __name__ == "__main__":
	el = '%20'.join(sys.argv[1:])
	search_url = "https://in.investing.com/search/?q="+el
	request_result=requests.get(search_url)
	header={'User-agent': 'Mozilla/5.0'}
	try:
		page=requests.get(search_url,headers=header)
		soup = BeautifulSoup(page.content,"html.parser")
		rs_details = soup.find("a", {"class": "tr common-table-item"})
		if rs_details.find("span", {"class": "td col-type"}).text != 'Share - NSE':
			raise Exception('Keyword not specific.')	
		stock_link = rs_details.get("href")
		stock_name = rs_details.find("span", {"class": "td col-name"}).text
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
	